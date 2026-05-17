from django.contrib import admin
from .models import SupportTicket


@admin.register(SupportTicket)
class SupportTicketAdmin(admin.ModelAdmin):
    list_display = ['user', 'subject', 'status', 'created_at']
    list_filter = ['status']
    search_fields = ['user__username', 'subject']
    fields = ['user', 'subject', 'message', 'status', 'admin_reply']
    readonly_fields = ['user', 'subject', 'message']
    actions = ['close_tickets']

    def close_tickets(self, request, queryset):
        queryset.update(status='closed')
    close_tickets.short_description = 'Close selected tickets'
