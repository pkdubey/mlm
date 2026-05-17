from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from core.services.wallet_service import get_all_balances
from core.services.tree_service import get_direct_team, get_full_downline, get_team_business
from core.services.rank_service import get_current_rank
from apps.wallets.models import WalletTransaction, WALLET_CHOICES

try:
    from weasyprint import HTML
    WEASYPRINT_AVAILABLE = True
except ImportError:
    WEASYPRINT_AVAILABLE = False


@login_required
def export_pdf(request):
    """Generate and download PDF report"""
    user = request.user
    balances = get_all_balances(user.id)
    total_income = sum(balances.get(w[0], 0) for w in WALLET_CHOICES if w[0] not in ['topup'])
    txns = WalletTransaction.objects.filter(user=user)[:50]
    context = {
        'user': user,
        'balances': balances,
        'wallet_choices': WALLET_CHOICES,
        'total_income': total_income,
        'txns': txns,
        'direct_count': get_direct_team(user.id).count(),
        'total_team': len(get_full_downline(user.id)),
        'team_business': get_team_business(user.id),
        'rank': get_current_rank(user.id),
    }
    
    # Generate PDF
    if WEASYPRINT_AVAILABLE:
        html_string = render_to_string('reports/income_report.html', context)
        pdf = HTML(string=html_string).write_pdf()
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="report_{user.username}.pdf"'
        return response
    
    # Fallback: show HTML version
    return render(request, 'reports/income_report.html', context)


@login_required
def report_preview(request):
    """Preview report in browser with sidebar/topbar"""
    user = request.user
    balances = get_all_balances(user.id)
    total_income = sum(balances.get(w[0], 0) for w in WALLET_CHOICES if w[0] not in ['topup'])
    txns = WalletTransaction.objects.filter(user=user)[:50]
    context = {
        'user': user,
        'balances': balances,
        'wallet_choices': WALLET_CHOICES,
        'total_income': total_income,
        'txns': txns,
        'direct_count': get_direct_team(user.id).count(),
        'total_team': len(get_full_downline(user.id)),
        'team_business': get_team_business(user.id),
        'rank': get_current_rank(user.id),
    }
    return render(request, 'reports/report_preview.html', context)
