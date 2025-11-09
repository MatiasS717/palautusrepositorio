import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Suomalaiset pelaajat:")

    järjestetty = sorted(players, key=lambda p: p.goals + p.assists, reverse=True)

    for player in järjestetty:
        if player.nationality == "FIN":
            print(player)

main()
