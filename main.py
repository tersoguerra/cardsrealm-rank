from datetime import date
from services.cardsrealm import CardsRealm
from dao.dataframe import *


def rank_teams():
    print("STARTING CARDSREALM TEAMS RANKING")
    cr = CardsRealm()

    teams_dict = cr.get_teams()
    teams_table = [["Time", "URL", "Torneios", "Partidas", "Pontos", "Vitórias", "Derrotas", "Empates",
                    "Jogadores", "Taxa de Vitória (%)"]]

    for team_name, team_dict in teams_dict.items():
        team_url = team_dict["url"]
        team_metrics, _ = cr.get_team_metrics_and_players(team_url)
        team_dict["metrics"] = team_metrics

        team_row = [team_name, team_url] + team_metrics
        teams_table.append(team_row)

        print(f"Team Name: {team_name}\nTeam URL: {team_url}\nTeam Metrics: {team_metrics}\n")

    csv_name = f"cardsrealm_teams_rank_{date.today()}.csv"
    sort_and_export(teams_table, "Pontos", csv_name)


def rank_teams_players():
    print("STARTING CARDSREALM TEAMS PLAYERS RANKING")
    cr = CardsRealm()

    teams_dict = cr.get_teams()
    players_urls = list()
    players_table = [["Usuário", "Torneiros", "Matchs", "Vitórias", "Derrotas", "Empates", "Pontos",
                      "Taxa de vitória", "URL"]]

    for team_name, team_dict in teams_dict.items():
        team_url = team_dict["url"]
        _, team_players = cr.get_team_metrics_and_players(team_url)
        players_urls = players_urls + team_players

        print(f"Team Name: {team_name}\nTeam URL: {team_url}\n")

    for player_url in players_urls:
        player_metrics = cr.get_player_metrics(player_url)
        player_metrics = player_metrics + [player_url]
        players_table.append(player_metrics)

        if len(player_metrics) > 2:
            print(f"Player Username: {player_metrics[0]}\nPlayer URL: {player_metrics[-1]}\n"
                  f"Player Metrics: {player_metrics[1:-1]}\n")

    csv_name = f"cardsrealm_players_rank_{date.today()}.csv"
    sort_and_export(players_table, "Pontos", csv_name)


if __name__ == "__main__":
    rank_teams()
