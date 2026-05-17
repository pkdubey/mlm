from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import random

WALLET_CHOICES = [
    ('income', 'Income Wallet'),
    ('self_income', 'Self Income Wallet'),
    ('booster', 'Booster Income Wallet'),
    ('star', 'Star Income Wallet'),
    ('trading_level', 'Trading Level Income Wallet'),
    ('salary', 'Salary Wallet'),
    ('reward', 'Reward Income'),
    ('growth', 'Growth Income Wallet'),
    ('sponsor_growth', 'Sponsor Growth Income'),
    ('usdt', 'USDT Wallet'),
    ('topup', 'Topup Wallet'),
]

TXN_CHOICES = [('credit', 'Credit'), ('debit', 'Debit')]


class WalletTransaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wallet_txns')
    wallet_type = models.CharField(max_length=30, choices=WALLET_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    txn_type = models.CharField(max_length=10, choices=TXN_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} | {self.wallet_type} | {self.txn_type} | {self.amount}"


class WalletTransfer(models.Model):
    from_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transfers_sent')
    to_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='transfers_received')
    from_wallet = models.CharField(max_length=30, choices=WALLET_CHOICES)
    to_wallet = models.CharField(max_length=30, choices=WALLET_CHOICES)
    amount = models.DecimalField(max_digits=15, decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.from_user} → {self.to_user} | {self.amount}"


class OTP(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='otps')
    otp_code = models.CharField(max_length=6)
    purpose = models.CharField(max_length=20, choices=[
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer'),
    ])
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    
    class Meta:
        ordering = ['-created_at']
    
    def save(self, *args, **kwargs):
        if not self.otp_code:
            self.otp_code = str(random.randint(100000, 999999))
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(minutes=10)
        super().save(*args, **kwargs)
    
    def is_valid(self):
        return not self.is_verified and timezone.now() < self.expires_at
    
    def __str__(self):
        return f"{self.user.username} - {self.otp_code} - {self.purpose}"
