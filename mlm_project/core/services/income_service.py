from apps.users.models import User
from core.services.wallet_service import credit_wallet


class IncomeService:

    def direct_income(self, new_user_id, amount):
        user = User.objects.get(id=new_user_id)
        if user.sponsor:
            credit_wallet(user.sponsor.id, 'income', amount * 0.10, 'Direct Income')

    def self_income(self, user_id, amount):
        credit_wallet(user_id, 'self_income', amount, 'Self Income')

    def booster_income(self, user_id, amount):
        credit_wallet(user_id, 'booster', amount, 'Booster Income')

    def star_income(self, user_id, amount):
        credit_wallet(user_id, 'star', amount, 'Star Income')

    def trading_level_income(self, user_id, level, amount):
        credit_wallet(user_id, 'trading_level', amount, f'Level {level} Income')

    def salary_income(self, user_id, amount):
        credit_wallet(user_id, 'salary', amount, 'Salary')

    def reward_income(self, user_id, amount):
        credit_wallet(user_id, 'reward', amount, 'Reward Income')

    def growth_income(self, user_id, amount):
        credit_wallet(user_id, 'growth', amount, 'Growth Income')

    def sponsor_growth_income(self, user_id, amount):
        credit_wallet(user_id, 'sponsor_growth', amount, 'Sponsor Growth Income')

    def level_income(self, trigger_user_id, investment, levels=10):
        LEVEL_PERCENT = [0.05, 0.03, 0.02, 0.01, 0.01, 0.01, 0.01, 0.01, 0.005, 0.005]
        user = User.objects.get(id=trigger_user_id)
        for i, pct in enumerate(LEVEL_PERCENT):
            user = User.objects.filter(id=user.sponsor_id).first()
            if not user:
                break
            credit_wallet(user.id, 'trading_level', investment * pct, f'Level {i+1} Income')
