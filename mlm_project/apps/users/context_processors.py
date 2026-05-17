from .models import Activity


def notifications_context(request):
    """Add notifications to all templates"""
    if request.user.is_authenticated:
        try:
            recent_activities = Activity.objects.filter(user=request.user)[:5]
            unread_count = Activity.objects.filter(user=request.user, is_read=False).count()
            return {
                'recent_activities': recent_activities,
                'unread_count': unread_count,
            }
        except Exception as e:
            # If table doesn't exist or any error, return empty
            return {
                'recent_activities': [],
                'unread_count': 0,
            }
    return {}
