from services.cardsrealm import CardsRealm


def rank_teams():
    cr = CardsRealm()

    teams_dict = cr.get_teams()

    for team_name, team_dict in teams_dict.items():
        team_url = team_dict["url"]
        team_metrics = cr.get_team_metrics(team_url)
        team_dict["metrics"] = team_metrics
        print(f"Team Name: {team_name}\nTeam URL: {team_url}\nTeam Metrics: {team_metrics}\n\n\n")


if __name__ == "__main__":
    rank_teams()
