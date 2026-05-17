from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from core.services.tree_service import get_direct_team, get_full_downline, get_level_team, build_tree_json


@login_required
def direct_team(request):
    team = get_direct_team(request.user.id)
    return render(request, 'genealogy/direct.html', {'team': team})


@login_required
def level_team(request):
    level = int(request.GET.get('level', 1))
    team = get_level_team(request.user.id, level)
    return render(request, 'genealogy/level.html', {'team': team, 'level': level, 'range': range(1, 11)})


@login_required
def genealogy_tree(request):
    tree_data = build_tree_json(request.user.id)
    return render(request, 'genealogy/tree.html', {'tree_data': tree_data})


@login_required
def whole_tree(request):
    downline = get_full_downline(request.user.id)
    return render(request, 'genealogy/whole_tree.html', {'downline': downline, 'total': len(downline)})
