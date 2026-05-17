from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.conf import settings
from apps.users.models import User
from core.services.wallet_service import get_all_balances
from datetime import datetime


class Command(BaseCommand):
    help = 'Send daily income report to all users'

    def handle(self, *args, **kwargs):
        users = User.objects.filter(is_active=True)
        sent_count = 0
        
        for user in users:
            try:
                balances = get_all_balances(user.id)
                total_income = sum(balances.values())
                
                subject = f'Daily Income Report - {datetime.now().strftime("%d %B %Y")}'
                message = f"""
Hello {user.username},

Here's your daily income summary:

Total Income: ₹{total_income:.2f}
Income Wallet: ₹{balances.get('income', 0):.2f}
Topup Wallet: ₹{balances.get('topup', 0):.2f}
USDT Wallet: ${balances.get('usdt', 0):.4f}

Keep growing your network!

Best regards,
MLM Network Team
                """
                
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL if hasattr(settings, 'DEFAULT_FROM_EMAIL') else 'noreply@mlm.com',
                    [user.email],
                    fail_silently=False,
                )
                sent_count += 1
                self.stdout.write(self.style.SUCCESS(f'Sent report to {user.email}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to send to {user.email}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully sent {sent_count} reports'))
