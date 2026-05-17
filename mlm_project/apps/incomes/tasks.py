from celery import shared_task


@shared_task
def process_direct_income(new_user_id, amount):
    from core.services.income_service import IncomeService
    IncomeService().direct_income(new_user_id, amount)


@shared_task
def process_level_income(trigger_user_id, investment):
    from core.services.income_service import IncomeService
    IncomeService().level_income(trigger_user_id, investment)


@shared_task
def process_self_income(user_id, amount):
    from core.services.income_service import IncomeService
    IncomeService().self_income(user_id, amount)
