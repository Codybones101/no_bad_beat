import requests
# from main_app.models import Game


r = requests.get('https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=78f8895d14199e90b32479676f2e1912&regions=us&oddsFormat=american&bookmakers=draftkings')
r.status_code

formatted = r.json()
bookmakers = formatted[0]['bookmakers']
markets = bookmakers[0]['markets']
outcomes = markets[0]['outcomes']

print(outcomes)
for game in formatted:
    print(f"Game Id: {game['id']}")
    print(f"AwayTeam: {game['away_team']}")
    print(f"HomeTeam: {game['home_team']}")
    # indivdual_game = Game(
    #     game_id=game['id'], away_team=game['away_team'], home_team=game['home_team'])
    # print(indivdual_game)

    for time in markets:
        print(f"LastUpdated: {time['last_update']}")
        for items in outcomes:
            print(f"Price: {items['price']}")
