from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from home.models import Topbar,  Footer
from.models import Team, Teamhead

def index(request):
  teams = Team.objects.order_by('-timestamp').filter(is_published=True)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  teamheads = Teamhead.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]
  paginator = Paginator(teams, 6)
  page = request.GET.get('page')
  paged_teams = paginator.get_page(page)


  context = {
    'teams': paged_teams,
    'topbars': topbars,
    'teamheads': teamheads,
    'footers': footers
  }

  return render(request, 'teams/teams.html', context)

def team(request, team_id):
  team = get_object_or_404(team, pk=team_id)
  topbars = Topbar.objects.order_by('-reload').filter(is_published=True)[:1]
  teamheads = Teamhead.objects.order_by('-reload').filter(is_published=True)[:1]
  footers = Footer.objects.order_by('-reload').filter(is_published=True)[:1]

  context = {
    'team': team,
    'topbars': topbars,
    'teamheads': teamheads,
    'footers': footers
  }

  return render(request, 'teams/team.html', context)

