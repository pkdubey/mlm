from django import forms
from .models import Deposit, Withdrawal
from apps.wallets.models import WALLET_CHOICES


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount', 'screenshot']


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['amount', 'wallet_type', 'upi_or_address']
        widgets = {
            'wallet_type': forms.Select(choices=WALLET_CHOICES),
        }
