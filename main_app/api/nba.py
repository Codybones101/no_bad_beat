import requests

r = requests.get('https://api.the-odds-api.com/v4/sports/basketball_nba/odds/?apiKey=78f8895d14199e90b32479676f2e1912&regions=us&oddsFormat=american&bookmakers=draftkings')
r.status_code

formatted = r.json()
bookmakers = formatted[0]['bookmakers']
markets = bookmakers[0]['markets']
outcomes = markets[0]['outcomes']


for game in formatted:
    print(game['id'], game['home_team'], game['away_team'])
    for time in markets:
        print(time['last_update'])
        for items in outcomes:
            print(items['price'])