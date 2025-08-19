import pandas as pd

year = 2025

while year <= 2025:
    advanced = pd.read_csv(f"advanced/{year-1}-{year}-advanced-stats.csv")
    pergame = pd.read_csv(f"per-game/{year-1}-{year}-per-game-stats.csv")
    voting = pd.read_csv(f"mvp-voting/{year-1}-{year}-mvp-voting.csv")
    standings = pd.read_csv(
        f"team-standings/{year-1}-{year}-team-standings.csv")

    output = pd.merge(advanced, pergame, on=[
                      "Player", "Age", "Team", "Pos", "G", "GS"], )

    year += 1
