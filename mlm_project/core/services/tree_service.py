from apps.users.models import User
from django.db.models import Sum


def get_direct_team(user_id):
    return User.objects.filter(sponsor_id=user_id)


def get_full_downline(user_id):
    visited = []
    queue = [user_id]
    while queue:
        current = queue.pop(0)
        children = User.objects.filter(sponsor_id=current)
        visited.extend(children)
        queue.extend([c.id for c in children])
    return visited


def get_level_team(user_id, level):
    current_level = [user_id]
    for _ in range(level):
        next_level = list(
            User.objects.filter(sponsor_id__in=current_level).values_list('id', flat=True)
        )
        if not next_level:
            return User.objects.none()
        current_level = next_level
    return User.objects.filter(id__in=current_level)


def get_team_business(user_id):
    downline = get_full_downline(user_id)
    ids = [u.id for u in downline]
    result = User.objects.filter(id__in=ids).aggregate(total=Sum('investment'))
    return result['total'] or 0


def build_tree_json(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return {}

    def build_node(u, depth=0):
        if depth > 5:
            return {'id': u.id, 'name': u.username, 'children': []}
        children = User.objects.filter(sponsor_id=u.id)
        return {
            'id': u.id,
            'name': u.username,
            'children': [build_node(c, depth + 1) for c in children]
        }

    return build_node(user)
