from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.services.wallet_service import get_all_balances
from apps.wallets.models import WalletTransaction, WALLET_CHOICES

INCOME_WALLETS = [w for w in WALLET_CHOICES if w[0] not in ['usdt', 'topup']]


@login_required
def income_summary(request):
    balances = get_all_balances(request.user.id)
    total = sum(balances.get(w[0], 0) for w in INCOME_WALLETS)
    recent_txns = WalletTransaction.objects.filter(
        user=request.user, txn_type='credit'
    ).exclude(wallet_type__in=['usdt', 'topup'])[:20]
    return render(request, 'incomes/summary.html', {
        'balances': balances,
        'income_wallets': INCOME_WALLETS,
        'total': total,
        'recent_txns': recent_txns,
    })
