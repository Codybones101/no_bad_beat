import requests
# from ..models import Game
# from main_app.models import Game
from .models import Game

def update_games():
    r = requests.get('https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=78f8895d14199e90b32479676f2e1912&regions=us&oddsFormat=american&bookmakers=draftkings')

    formatted = r.json()
    bookmakers = formatted[0]['bookmakers']
    markets = bookmakers[0]['markets']
    outcomes = markets[0]['outcomes']

    for game in formatted:
        bookmakers = game['bookmakers'][0]
        markets = bookmakers['markets']
        outcomes = markets[0]['outcomes']

        if Game.objects.filter(game_id = game['id']):
                update_game = Game.objects.filter(game_id = game['id'])
                update_game.update(
                    away_price = outcomes[0]['price'],
                    home_price = outcomes[1]['price'],
                )
        else:
            new_game = Game(
                game_id = game['id'],
                away_team = game['away_team'],
                home_team = game['home_team'],
                away_price = outcomes[0]['price'],
                home_price = outcomes[1]['price'],
            )
            new_game.save()