from django import forms
from .models import WalletTransfer, WALLET_CHOICES
from apps.users.models import User


class WalletTransferForm(forms.Form):
    to_username = forms.CharField(max_length=150, label='Recipient Username')
    from_wallet = forms.ChoiceField(choices=WALLET_CHOICES)
    to_wallet = forms.ChoiceField(choices=WALLET_CHOICES)
    amount = forms.DecimalField(max_digits=15, decimal_places=4, min_value=0.0001)

    def clean_to_username(self):
        username = self.cleaned_data['to_username']
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError('User not found.')
