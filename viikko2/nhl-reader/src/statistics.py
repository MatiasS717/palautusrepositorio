import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        self.url = url
    
    def get_players(self):
        url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
        response = requests.get(url).json()

        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players

class PlayerStats:

    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        järjestetty = sorted(self.players, key=lambda p: p.goals + p.assists, reverse=True)

        top_scorers = []

        for player in järjestetty:
            if player.nationality == nationality:
                top_scorers.append(player)
        return top_scorers

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

main()

