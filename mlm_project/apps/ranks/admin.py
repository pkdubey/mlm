from django.contrib import admin
from .models import Rank


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ['user', 'rank_name', 'achieved_at', 'reward_given']
    list_filter = ['rank_name', 'reward_given']
    actions = ['mark_reward_given']

    def mark_reward_given(self, request, queryset):
        queryset.update(reward_given=True)
    mark_reward_given.short_description = 'Mark reward as given'
