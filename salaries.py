import pandas as pd
from pathlib import Path
import csv

class GetSalaries:
    def __init__(self):
        self.path = Path('./static_data/mlb_salaries.xlsx')
        self.df = pd.read_excel(self.path)

    def get_salaries_df(self):
        df = self.df
        columns = ["Name", "Position", "Service Time", "Salary"]
        df = df.drop(0)
        df.columns = columns

        return df.dropna()

class CleanSalaryData:
    def clean_salary_names(df):
        new_names = []
        for player in df['Name']:
            player = player.replace(",", "")
            player = player.replace(" Jr.", "")
            player = player.replace("La ", "La")
            player = player.replace("Michael A.", "MichaelA.")
            player = player.replace("Jean Carlos", "JeanCarlos")
            player = player.replace("De ", "De")
            player = player.replace("de Geus", "deGeus")
            player = player.replace("Chi Chi", "ChiChi")
            player = player.replace(" de", "de")
            player = player.replace(" O.", "")
            player = player.replace(" L.", "")
            new_names.append(player)
        df["Name"] = new_names
        return df

    def switch_last_first(df):
        new_names = []
        for player in df["Name"]:
            new_name = ""
            for i in range(len(player)):
                if player[i] == " ":
                    first_name = player[(i + 1):]
                    last_name = player[0:i]
                    new_name = first_name + " " + last_name
                    new_names.append(new_name)
        df["Name"] = new_names
        return df

