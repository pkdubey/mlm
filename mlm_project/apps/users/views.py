from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from core.services.wallet_service import get_balance, get_all_balances
from core.services.tree_service import get_direct_team, get_full_downline, get_team_business
from core.services.rank_service import get_current_rank
from apps.wallets.models import WALLET_CHOICES
from .forms import RegisterForm, ProfileUpdateForm
from .models import User, Activity, LandingPageContent

WALLET_TYPES = [w[0] for w in WALLET_CHOICES]


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    
    try:
        content = LandingPageContent.objects.filter(is_active=True).first()
        if not content:
            content = LandingPageContent.objects.create()
    except:
        content = None
    
    context = {'content': content}
    return render(request, 'users/landing.html', context)


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Log activity for sponsor if exists
            if user.sponsor:
                from .activity_helpers import log_member_joined
                log_member_joined(user.sponsor, user)
            
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('dashboard')
    else:
        ref = request.GET.get('ref', '')
        form = RegisterForm(initial={'referral_code': ref})
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    user = request.user
    balances = get_all_balances(user.id)
    total_income = sum(balances.get(w, 0) for w in WALLET_TYPES if w not in ['topup'])
    direct_team = get_direct_team(user.id)
    full_downline = get_full_downline(user.id)
    
    # Get recent activities (last 10)
    try:
        recent_activities = Activity.objects.filter(user=user)[:10]
        unread_count = Activity.objects.filter(user=user, is_read=False).count()
    except:
        recent_activities = []
        unread_count = 0
    
    # Calculate growth metrics (last 7 days vs previous 7 days)
    from django.utils import timezone
    from datetime import timedelta
    from apps.wallets.models import WalletTransaction
    
    now = timezone.now()
    week_ago = now - timedelta(days=7)
    two_weeks_ago = now - timedelta(days=14)
    
    # This week's income
    this_week_income = WalletTransaction.objects.filter(
        user=user,
        txn_type='credit',
        created_at__gte=week_ago
    ).aggregate(total=models.Sum('amount'))['total'] or 0
    
    # Last week's income
    last_week_income = WalletTransaction.objects.filter(
        user=user,
        txn_type='credit',
        created_at__gte=two_weeks_ago,
        created_at__lt=week_ago
    ).aggregate(total=models.Sum('amount'))['total'] or 0
    
    # Calculate growth percentage
    if last_week_income > 0:
        income_growth = ((this_week_income - last_week_income) / last_week_income) * 100
    else:
        income_growth = 100 if this_week_income > 0 else 0
    
    # New members this week
    new_members_this_week = User.objects.filter(
        sponsor=user,
        date_joined__gte=week_ago
    ).count()
    
    # New members last week
    new_members_last_week = User.objects.filter(
        sponsor=user,
        date_joined__gte=two_weeks_ago,
        date_joined__lt=week_ago
    ).count()
    
    context = {
        'balances': balances,
        'wallet_choices': WALLET_CHOICES,
        'total_income': total_income,
        'direct_count': direct_team.count(),
        'total_team': len(full_downline),
        'team_business': get_team_business(user.id),
        'rank': get_current_rank(user.id),
        'referral_link': request.build_absolute_uri(f'/auth/register/?ref={user.referral_code}'),
        'recent_activities': recent_activities,
        'unread_count': unread_count,
        'income_growth': round(income_growth, 1),
        'new_members_this_week': new_members_this_week,
        'new_members_last_week': new_members_last_week,
        'this_week_income': this_week_income,
    }
    return render(request, 'users/dashboard.html', context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    direct_team = get_direct_team(request.user.id)
    full_downline = get_full_downline(request.user.id)
    context = {
        'form': form,
        'direct_count': direct_team.count(),
        'total_team': len(full_downline),
        'team_business': get_team_business(request.user.id),
        'referral_link': request.build_absolute_uri(f'/auth/register/?ref={request.user.referral_code}'),
    }
    return render(request, 'users/profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password changed successfully.')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})
