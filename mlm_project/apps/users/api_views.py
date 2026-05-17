from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from apps.users.models import User
from apps.wallets.models import WalletTransaction


@login_required
def global_search(request):
    query = request.GET.get('q', '').strip()
    results = []
    
    if len(query) < 2:
        return JsonResponse({'results': results})
    
    # Search Users
    users = User.objects.filter(
        Q(username__icontains=query) | 
        Q(email__icontains=query) |
        Q(referral_code__icontains=query)
    )[:5]
    
    for user in users:
        results.append({
            'title': user.username,
            'subtitle': f'ID: {user.id} | Email: {user.email}',
            'url': f'/profile/',  # You can create user detail page
            'icon': 'bi-person-circle'
        })
    
    # Search Transactions
    transactions = WalletTransaction.objects.filter(
        user=request.user,
        description__icontains=query
    )[:5]
    
    for txn in transactions:
        results.append({
            'title': f'{txn.get_wallet_type_display()} - ₹{txn.amount}',
            'subtitle': f'{txn.description} | {txn.created_at.strftime("%d %b %Y")}',
            'url': '/wallets/history/',
            'icon': 'bi-cash-stack'
        })
    
    # Add quick links based on query
    quick_links = {
        'wallet': {'title': 'All Wallets', 'url': '/wallets/', 'icon': 'bi-wallet2'},
        'team': {'title': 'Direct Team', 'url': '/team/direct/', 'icon': 'bi-people'},
        'income': {'title': 'Income Summary', 'url': '/incomes/summary/', 'icon': 'bi-cash-stack'},
        'rank': {'title': 'Rank & Reward', 'url': '/ranks/', 'icon': 'bi-trophy'},
        'support': {'title': 'Support Tickets', 'url': '/support/', 'icon': 'bi-headset'},
        'transfer': {'title': 'Transfer Wallet', 'url': '/wallets/transfer/', 'icon': 'bi-arrow-left-right'},
    }
    
    for key, link in quick_links.items():
        if key in query.lower():
            results.insert(0, {
                'title': link['title'],
                'subtitle': 'Quick Link',
                'url': link['url'],
                'icon': link['icon']
            })
    
    return JsonResponse({'results': results[:10]})
