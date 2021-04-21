import pandas as pd
from datetime import date
from services.cardsrealm import CardsRealm


def rank_teams():
    cr = CardsRealm()

    teams_dict = cr.get_teams()
    teams_table = [["Time", "URL", "Torneios", "Partidas", "Pontos", "Vitórias", "Derrotas", "Empates",
                    "Jogadores", "Taxa de Vitória (%)"]]

    for team_name, team_dict in teams_dict.items():
        team_url = team_dict["url"]
        team_metrics = cr.get_team_metrics(team_url)
        team_dict["metrics"] = team_metrics

        team_row = [team_name, team_url] + team_metrics
        teams_table.append(team_row)

        print(f"Team Name: {team_name}\nTeam URL: {team_url}\nTeam Metrics: {team_metrics}\n\n")

    teams_df = pd.DataFrame(teams_table, columns=teams_table.pop(0))
    teams_df.sort_values(by=['Pontos'], inplace=True, ascending=False)

    csv_name = f"cardsrealm_teams_rank_{date.today()}.csv"
    teams_df.to_csv(csv_name, index=False)


if __name__ == "__main__":
    rank_teams()
