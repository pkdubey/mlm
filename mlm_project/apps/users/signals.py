from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User


@receiver(post_save, sender=User)
def on_user_created(sender, instance, created, **kwargs):
    if created and instance.sponsor:
        try:
            from core.services.income_service import IncomeService
            svc = IncomeService()
            svc.direct_income(instance.id, float(instance.investment))
            svc.level_income(instance.id, float(instance.investment))
        except Exception:
            pass
