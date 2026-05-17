from core.services.tree_service import get_full_downline, get_team_business
from apps.ranks.models import Rank

RANK_CRITERIA = [
    {'name': 'Silver',  'team': 10,  'business': 50000},
    {'name': 'Gold',    'team': 25,  'business': 150000},
    {'name': 'Diamond', 'team': 50,  'business': 500000},
    {'name': 'Crown',   'team': 100, 'business': 1000000},
]


def get_current_rank(user_id):
    rank = Rank.objects.filter(user_id=user_id).order_by('-achieved_at').first()
    return rank.rank_name if rank else 'No Rank'


def assign_rank(user_id, rank_name):
    if not Rank.objects.filter(user_id=user_id, rank_name=rank_name).exists():
        Rank.objects.create(user_id=user_id, rank_name=rank_name)


def check_and_assign_rank(user_id):
    team_count = len(get_full_downline(user_id))
    team_business = get_team_business(user_id)
    for rank in reversed(RANK_CRITERIA):
        if team_count >= rank['team'] and team_business >= rank['business']:
            assign_rank(user_id, rank['name'])
            break
