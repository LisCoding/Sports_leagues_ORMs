from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	# context = {
	# 	"leagues": League.objects.all(),
	# 	"teams": Team.objects.all(),
	# 	"players": Player.objects.all(),
	# }
	baseball=[]
	women = League.objects.filter(name__contains="womens").values("name")
	hockey = League.objects.filter(name__contains="hockey").values("name")
	nofootball = League.objects.exclude(name="football").values("name")
	conference = League.objects.filter(name__contains="conference").values("name")
	atlantic = League.objects.filter(name__contains="Atlantic").values("name")
	dallas = Team.objects.filter(location="Dallas")
	raptors = Team.objects.filter(team_name__contains="Raptors")
	city = Team.objects.filter(location__contains="City")
	T = Team.objects.filter(team_name__startswith="T")
	order_loc =  Team.objects.order_by("location")
	order_name = Team.objects.order_by("-team_name")
	l_name_cooper = Player.objects.filter(last_name__contains="Cooper")
	n_joshua = Player.objects.filter(first_name__contains="Joshua")
	exclude_joshua = Player.objects.filter(last_name__contains="Cooper").exclude(first_name="Joshua")
	Alex_or_Wy= Player.objects.filter(first_name="Alexander")|Player.objects.filter(first_name="Wyatt")
	for sport in League.objects.filter(sport="Baseball"):
		baseball += [sport.name]

	context = {
		"baseball": baseball,
		"women": women,
		"hockey": hockey,
		"nofootball": nofootball,
		"conferences":conference,
		"atlantic": atlantic,
		"dallas": dallas,
		"raptors": raptors,
		"city": city,
		"T": T,
		"order_loc" : order_loc,
		"order_name": order_name,
		"l_name_cooper": l_name_cooper,
		"n_joshua": n_joshua,
		"exclude_joshua": exclude_joshua,
		"Alex_or_Wy" : Alex_or_Wy

	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
