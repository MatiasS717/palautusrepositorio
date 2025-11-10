import requests
from rich.console import Console
from rich.table import Table
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
        jarjestetty = sorted(self.players, key=lambda p: p.goals + p.assists, reverse=True)

        top_scorers = []

        for player in jarjestetty:
            if player.nationality == nationality:
                top_scorers.append(player)
        return top_scorers

class TableCreator:

    def __init__(self, stats, nationality, season):
        self.players = stats.top_scorers_by_nationality(nationality)
        self.season = season
        self.nationality = nationality

    def return_table(self):
        table = Table(title=f"Season {self.season} players from {self.nationality}")

        table.add_column("Player", style="cyan", no_wrap=True)
        table.add_column("Teams", style="magenta")
        table.add_column("Goals", style="green")
        table.add_column("Assists", style="green")
        table.add_column("Points", style="green")

        for player in self.players:
            table.add_row(player.name, player.team, str(player.goals),
                          str(player.assists), str(player.points))

        console = Console()
        console.print(table)


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    TableCreator(stats, "FIN", "2024-2025").return_table()

main()
