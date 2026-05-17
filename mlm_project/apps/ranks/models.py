from django.db import models
from django.conf import settings


class Rank(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ranks')
    rank_name = models.CharField(max_length=50)
    achieved_at = models.DateField(auto_now_add=True)
    reward_given = models.BooleanField(default=False)

    class Meta:
        ordering = ['-achieved_at']

    def __str__(self):
        return f"{self.user.username} - {self.rank_name}"
