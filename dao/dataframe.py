import pandas as pd


def sort_and_export(table, sort_column, file_name):
    teams_df = pd.DataFrame(table, columns=table.pop(0))

    teams_df.sort_values(by=[sort_column], inplace=True, ascending=False)

    teams_df.to_csv(file_name, index=False)
