from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Comment, Bet
from .forms import CommentForm
from .forms import BetForm
from django.views.generic.edit import UpdateView, DeleteView

team_list = {
    'Atlanta Hawks': '../static/images/nba_logos/AtlantaHawks.png',
    'Boston Celtics': '../static/images/nba_logos/BostonCeltics.png',
    'Brooklyn Nets': '../static/images/nba_logos/BrooklynNets.png',
    'Charlotte Hornets': '../static/images/nba_logos/CharoletteHornets.png',
    'Chicago Bulls': '../static/images/nba_logos/ChicagoBulls.png',
    'Clevland Cavaliers': '../static/images/nba_logos/ClevlandCavaliers.png',
    'Dallas Maverics': '../static/images/nba_logos/DallasMaverics.png',
    'Denver Nuggets': '../static/images/nba_logos/DenverNuggets.png',
    'Detroit Pistons': '../static/images/nba_logos/DetroitPistons.png',
    'Golden State Warriors': '../static/images/nba_logos/GoldenStateWarriors.png',
    'Houston Rockets': '../static/images/nba_logos/HoustonRockets.png',
    'Indiana Pacers': '../static/images/nba_logos/IndianaPacers.png',
    'Los Angeles Clippers': '../static/images/nba_logos/LosAngelesClippers.png',
    'Los Angeles Lakers': '../static/images/nba_logos/LosAngelesLakers.png',
    'Memphis Grizzlies': '../static/images/nba_logos/MemphisGrizzlies.png',
    'Miami Heat': '../static/images/nba_logos/MiamiHeat.png',
    'Milwaukee Bucks': '../static/images/nba_logos/MilwaukeeBucks.png',
    'Minnesota Timberwolves': '../static/images/nba_logos/MinnesotaTimberwolves.png',
    'New Oreleans Pelicans': '../static/images/nba_logos/NewOreleansPelicans.png',
    'New York Knicks': '../static/images/nba_logos/NewYorkKnicks.png',
    'Oklahoma City Thunder': '../static/images/nba_logos/OklahomaCityThunder.png',
    'Orlando Magic': '../static/images/nba_logos/OrlandoMagic.png',
    'Philadelphia 76ers': '../static/images/nba_logos/Philadelphia76ers.png',
    'Phoenix Suns': '../static/images/nba_logos/PhoenixSuns.png',
    'Portland Trail Blazers': '../static/images/nba_logos/PortlandTrailBlazers.png',
    'Sacramento Kings': '../static/images/nba_logos/SacramentoKings.png',
    'San Antonio Spurs': '../static/images/nba_logos/SanAntonioSpurs.png',
    'Toronto Raptors': '../static/images/nba_logos/TorontoRaptors.png',
    'Utah Jazz': '../static/images/nba_logos/UtahJazz.png',
    'Washington Wizards': '../static/images/nba_logos/WashingtonWizards.png',
}

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            # <--------------------------------------- We need to change this
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {
        'games': games
    })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    comment_form = CommentForm()
    return render(request, 'games/detail.html', {
        'game': game, 'comment_form': comment_form, 'away_team': team_list[game.away_team], 'home_team': team_list[game.home_team]
    })


@login_required
def add_comment(request, game_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.comment_user = request.user
        new_comment.game_id = game_id
        new_comment.game_choice = request.POST.get('game_choice')
        new_comment.save()
    return redirect('detail', game_id=game_id)

@login_required
def add_bet(request, game_id):
    form = BetForm(request.POST)
    if form.is_valid():
        new_bet = form.save(commit=False)
        new_bet.bet_user = request.user
        new_bet.game_id = game_id
        new_bet.save()
    return redirect('detail', game_id=game_id)

class CommentUpdate(UpdateView):
    model = Comment
    fields = ['comment']
    success_url = '/games/{game_id}'


class CommentDelete(DeleteView):
    model = Comment
    success_url = '/games/{game_id}'
