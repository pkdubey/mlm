from django.contrib import admin
from django.utils import timezone
from core.services.wallet_service import credit_wallet
from .models import Deposit, Withdrawal


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'status', 'created_at', 'approved_at']
    list_filter = ['status']
    actions = ['approve_deposits', 'reject_deposits']

    def approve_deposits(self, request, queryset):
        for dep in queryset.filter(status='pending'):
            credit_wallet(dep.user_id, 'topup', dep.amount, 'Deposit Approved')
            dep.status = 'approved'
            dep.approved_at = timezone.now()
            dep.save()
        self.message_user(request, 'Selected deposits approved.')
    approve_deposits.short_description = 'Approve selected deposits'

    def reject_deposits(self, request, queryset):
        queryset.filter(status='pending').update(status='rejected')
        self.message_user(request, 'Selected deposits rejected.')
    reject_deposits.short_description = 'Reject selected deposits'


@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ['user', 'amount', 'wallet_type', 'upi_or_address', 'status', 'created_at', 'paid_at']
    list_filter = ['status', 'wallet_type']
    actions = ['mark_paid', 'reject_withdrawals']

    def mark_paid(self, request, queryset):
        queryset.filter(status='pending').update(status='paid', paid_at=timezone.now())
        self.message_user(request, 'Marked as paid.')
    mark_paid.short_description = 'Mark as Paid'

    def reject_withdrawals(self, request, queryset):
        for w in queryset.filter(status='pending'):
            credit_wallet(w.user_id, w.wallet_type, w.amount, 'Withdrawal Rejected - Refund')
            w.status = 'rejected'
            w.save()
        self.message_user(request, 'Withdrawals rejected and refunded.')
    reject_withdrawals.short_description = 'Reject & Refund'
