from django.db import transaction
from django.db.models import Sum
from apps.wallets.models import WalletTransaction, WALLET_CHOICES


def get_balance(user_id, wallet_type):
    credits = WalletTransaction.objects.filter(
        user_id=user_id, wallet_type=wallet_type, txn_type='credit'
    ).aggregate(total=Sum('amount'))['total'] or 0
    debits = WalletTransaction.objects.filter(
        user_id=user_id, wallet_type=wallet_type, txn_type='debit'
    ).aggregate(total=Sum('amount'))['total'] or 0
    return credits - debits


def get_all_balances(user_id):
    return {w[0]: get_balance(user_id, w[0]) for w in WALLET_CHOICES}


def credit_wallet(user_id, wallet_type, amount, description=''):
    with transaction.atomic():
        WalletTransaction.objects.create(
            user_id=user_id, wallet_type=wallet_type,
            amount=amount, txn_type='credit', description=description
        )


def debit_wallet(user_id, wallet_type, amount, description=''):
    balance = get_balance(user_id, wallet_type)
    if balance < amount:
        raise ValueError('Insufficient balance')
    with transaction.atomic():
        WalletTransaction.objects.create(
            user_id=user_id, wallet_type=wallet_type,
            amount=amount, txn_type='debit', description=description
        )
