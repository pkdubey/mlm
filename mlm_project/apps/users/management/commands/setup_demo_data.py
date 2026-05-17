from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.wallets.models import WalletTransaction
from apps.users.models import Activity
from apps.users.activity_helpers import *
from decimal import Decimal
import random

User = get_user_model()


class Command(BaseCommand):
    help = 'Setup complete demo data with users, wallets, activities, and transactions'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Setting up demo data...'))
        
        # Create demo users with referral chain
        users_data = [
            {'username': 'john_doe', 'email': 'john@example.com', 'phone': '9876543210', 'investment': 10000},
            {'username': 'jane_smith', 'email': 'jane@example.com', 'phone': '9876543211', 'investment': 15000},
            {'username': 'mike_wilson', 'email': 'mike@example.com', 'phone': '9876543212', 'investment': 20000},
            {'username': 'sarah_jones', 'email': 'sarah@example.com', 'phone': '9876543213', 'investment': 12000},
            {'username': 'david_brown', 'email': 'david@example.com', 'phone': '9876543214', 'investment': 18000},
        ]
        
        created_users = []
        sponsor = None
        
        # Get existing admin user as main sponsor
        try:
            admin_user = User.objects.filter(is_superuser=True).first()
            if admin_user:
                sponsor = admin_user
                self.stdout.write(self.style.SUCCESS(f'Using {admin_user.username} as main sponsor'))
        except:
            pass
        
        # Create users
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data['username'],
                defaults={
                    'email': user_data['email'],
                    'phone': user_data['phone'],
                    'investment': user_data['investment'],
                    'sponsor': sponsor,
                }
            )
            
            if created:
                user.set_password('demo123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'Created user: {user.username}'))
                
                # Create activity for sponsor
                if sponsor:
                    log_member_joined(sponsor, user)
                
                created_users.append(user)
                sponsor = user  # Next user will be sponsored by this user
            else:
                self.stdout.write(self.style.WARNING(f'User {user.username} already exists'))
                created_users.append(user)
        
        # Add wallet balances and transactions
        wallet_types = [
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
        
        # Add transactions for all users (including admin)
        all_users = list(User.objects.all())
        
        for user in all_users:
            self.stdout.write(f'Adding wallet balances for {user.username}...')
            
            # Add topup wallet balance
            topup_amount = Decimal(random.randint(5000, 20000))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='topup',
                amount=topup_amount,
                txn_type='credit',
                description='Initial topup deposit'
            )
            log_deposit_made(user, topup_amount)
            
            # Add income wallet balances
            income_amount = Decimal(random.randint(2000, 8000))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='income',
                amount=income_amount,
                txn_type='credit',
                description='Direct referral income'
            )
            log_income_credited(user, income_amount, 'Income Wallet')
            
            # Add self income
            self_income = Decimal(random.randint(1000, 5000))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='self_income',
                amount=self_income,
                txn_type='credit',
                description='Self investment income'
            )
            log_income_credited(user, self_income, 'Self Income Wallet')
            
            # Add level income
            level_income = Decimal(random.randint(500, 3000))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='income',
                amount=level_income,
                txn_type='credit',
                description='Level 2 team income'
            )
            log_level_income(user, level_income, 2)
            
            # Add booster income
            booster_amount = Decimal(random.randint(300, 2000))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='booster',
                amount=booster_amount,
                txn_type='credit',
                description='Booster income from team'
            )
            log_income_credited(user, booster_amount, 'Booster Wallet')
            
            # Add star income
            star_amount = Decimal(random.randint(200, 1500))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='star',
                amount=star_amount,
                txn_type='credit',
                description='Star achiever income'
            )
            
            # Add reward
            reward_amount = Decimal(random.randint(500, 2500))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='reward',
                amount=reward_amount,
                txn_type='credit',
                description='Monthly performance reward'
            )
            log_reward_received(user, reward_amount, 'Performance')
            
            # Add USDT wallet
            usdt_amount = Decimal(random.randint(10, 100))
            WalletTransaction.objects.create(
                user=user,
                wallet_type='usdt',
                amount=usdt_amount,
                txn_type='credit',
                description='USDT conversion'
            )
            
            # Random rank upgrade for some users
            if random.choice([True, False]):
                ranks = ['Silver', 'Gold', 'Diamond']
                rank = random.choice(ranks)
                log_rank_upgraded(user, rank)
            
            # Random withdrawal request
            if random.choice([True, False]):
                withdrawal_amount = Decimal(random.randint(1000, 5000))
                log_withdrawal_requested(user, withdrawal_amount)
            
            self.stdout.write(self.style.SUCCESS(f'Added balances for {user.username}'))
        
        # Summary
        self.stdout.write(self.style.SUCCESS('\n' + '='*50))
        self.stdout.write(self.style.SUCCESS('Demo Data Setup Complete!'))
        self.stdout.write(self.style.SUCCESS('='*50))
        self.stdout.write(f'Total Users: {User.objects.count()}')
        self.stdout.write(f'Total Transactions: {WalletTransaction.objects.count()}')
        self.stdout.write(f'Total Activities: {Activity.objects.count()}')
        self.stdout.write(self.style.SUCCESS('\nDemo User Credentials:'))
        self.stdout.write('   Username: john_doe | Password: demo123')
        self.stdout.write('   Username: jane_smith | Password: demo123')
        self.stdout.write('   Username: mike_wilson | Password: demo123')
        self.stdout.write(self.style.SUCCESS('\nYou can now login and see the dashboard with real data!'))
