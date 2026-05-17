from django.db import models
from django.conf import settings
from apps.wallets.models import WALLET_CHOICES

STATUS_CHOICES = [('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')]
WITHDRAWAL_STATUS = [('pending', 'Pending'), ('paid', 'Paid'), ('rejected', 'Rejected')]


class Deposit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='deposits')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    screenshot = models.ImageField(upload_to='deposits/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    approved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} | {self.amount} | {self.status}"


class Withdrawal(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='withdrawals')
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    wallet_type = models.CharField(max_length=30, choices=WALLET_CHOICES)
    upi_or_address = models.CharField(max_length=200)
    status = models.CharField(max_length=10, choices=WITHDRAWAL_STATUS, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} | {self.amount} | {self.status}"
