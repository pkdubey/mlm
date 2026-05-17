from django.core.management.base import BaseCommand
from apps.users.models import User, Activity
from apps.users.activity_helpers import *
from decimal import Decimal


class Command(BaseCommand):
    help = 'Create sample activities for testing'

    def handle(self, *args, **kwargs):
        # Get all users
        users = User.objects.all()
        
        if not users.exists():
            self.stdout.write(self.style.ERROR('No users found. Please create users first.'))
            return
        
        created_count = 0
        
        for user in users:
            # Create sample activities for each user
            try:
                # Income credited
                log_income_credited(user, Decimal('500.00'), 'Income Wallet')
                created_count += 1
                
                # Deposit made
                log_deposit_made(user, Decimal('1000.00'))
                created_count += 1
                
                # Level income
                log_level_income(user, Decimal('300.00'), 2)
                created_count += 1
                
                # If user has sponsor, create member joined activity for sponsor
                if user.sponsor:
                    log_member_joined(user.sponsor, user)
                    created_count += 1
                
                # Rank upgraded (for some users)
                if user.id % 2 == 0:
                    log_rank_upgraded(user, 'Silver')
                    created_count += 1
                
                self.stdout.write(self.style.SUCCESS(f'Created activities for {user.username}'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Error for {user.username}: {str(e)}'))
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {created_count} sample activities'))
