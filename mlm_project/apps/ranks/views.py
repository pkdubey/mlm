from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.services.rank_service import get_current_rank, check_and_assign_rank, RANK_CRITERIA
from .models import Rank


@login_required
def rank_view(request):
    check_and_assign_rank(request.user.id)
    current_rank = get_current_rank(request.user.id)
    rank_history = Rank.objects.filter(user=request.user)
    return render(request, 'ranks/rank.html', {
        'current_rank': current_rank,
        'rank_history': rank_history,
        'rank_criteria': RANK_CRITERIA,
    })
