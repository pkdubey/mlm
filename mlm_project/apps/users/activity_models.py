from django.db import models
from django.conf import settings


ACTIVITY_TYPES = [
    ('member_joined', 'Member Joined'),
    ('income_credited', 'Income Credited'),
    ('withdrawal_requested', 'Withdrawal Requested'),
    ('withdrawal_approved', 'Withdrawal Approved'),
    ('withdrawal_rejected', 'Withdrawal Rejected'),
    ('deposit_made', 'Deposit Made'),
    ('transfer_sent', 'Transfer Sent'),
    ('transfer_received', 'Transfer Received'),
    ('rank_upgraded', 'Rank Upgraded'),
    ('level_income', 'Level Income'),
    ('direct_income', 'Direct Income'),
    ('reward_received', 'Reward Received'),
]


class Activity(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=30, choices=ACTIVITY_TYPES)
    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    related_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='related_activities')
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Activities'

    def __str__(self):
        return f"{self.user.username} - {self.title}"

    def get_icon(self):
        """Return Bootstrap icon class based on activity type"""
        icons = {
            'member_joined': 'bi-person-plus',
            'income_credited': 'bi-cash',
            'withdrawal_requested': 'bi-arrow-up-circle',
            'withdrawal_approved': 'bi-check-circle',
            'withdrawal_rejected': 'bi-x-circle',
            'deposit_made': 'bi-arrow-down-circle',
            'transfer_sent': 'bi-arrow-right-circle',
            'transfer_received': 'bi-arrow-left-circle',
            'rank_upgraded': 'bi-trophy',
            'level_income': 'bi-graph-up',
            'direct_income': 'bi-cash-stack',
            'reward_received': 'bi-gift',
        }
        return icons.get(self.activity_type, 'bi-info-circle')

    def get_color(self):
        """Return color class based on activity type"""
        colors = {
            'member_joined': 'success',
            'income_credited': 'success',
            'withdrawal_requested': 'warning',
            'withdrawal_approved': 'success',
            'withdrawal_rejected': 'danger',
            'deposit_made': 'info',
            'transfer_sent': 'info',
            'transfer_received': 'success',
            'rank_upgraded': 'success',
            'level_income': 'info',
            'direct_income': 'success',
            'reward_received': 'success',
        }
        return colors.get(self.activity_type, 'info')

    def time_ago(self):
        """Return human-readable time difference"""
        from django.utils import timezone
        from datetime import timedelta
        
        now = timezone.now()
        diff = now - self.created_at
        
        if diff < timedelta(minutes=1):
            return 'Just now'
        elif diff < timedelta(hours=1):
            minutes = int(diff.total_seconds() / 60)
            return f'{minutes} minute{"s" if minutes > 1 else ""} ago'
        elif diff < timedelta(days=1):
            hours = int(diff.total_seconds() / 3600)
            return f'{hours} hour{"s" if hours > 1 else ""} ago'
        elif diff < timedelta(days=7):
            days = diff.days
            return f'{days} day{"s" if days > 1 else ""} ago'
        elif diff < timedelta(days=30):
            weeks = int(diff.days / 7)
            return f'{weeks} week{"s" if weeks > 1 else ""} ago'
        else:
            months = int(diff.days / 30)
            return f'{months} month{"s" if months > 1 else ""} ago'
