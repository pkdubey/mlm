from django.contrib import admin
from .models import WalletTransaction, WalletTransfer, OTP


@admin.register(WalletTransaction)
class WalletTransactionAdmin(admin.ModelAdmin):
    list_display = ['user', 'wallet_type', 'txn_type', 'amount', 'description', 'created_at']
    list_filter = ['wallet_type', 'txn_type', 'created_at']
    search_fields = ['user__username', 'description']


@admin.register(WalletTransfer)
class WalletTransferAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user', 'from_wallet', 'to_wallet', 'amount', 'created_at']


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ['user', 'otp_code', 'purpose', 'is_verified', 'created_at', 'expires_at']
    list_filter = ['purpose', 'is_verified', 'created_at']
    search_fields = ['user__username', 'otp_code']
    readonly_fields = ['created_at']
