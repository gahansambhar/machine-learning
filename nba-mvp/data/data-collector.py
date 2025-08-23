import pandas as pd

year = 1980

output = pd.DataFrame()
# Loop through each year from 1980 to 2025
while year <= 2025:
    advanced = pd.read_csv(f"advanced/{year-1}-{year}-advanced-stats.csv")
    pergame = pd.read_csv(f"per-game/{year-1}-{year}-per-game-stats.csv")
    voting = pd.read_csv(f"mvp-voting/{year-1}-{year}-mvp-voting.csv")
    standings = pd.read_csv(
        f"team-standings/{year-1}-{year}-team-standings.csv")

    curr = pd.merge(pergame, advanced, on=[
                      "Player", "Age", "Team", "Pos", "G", "GS"], )
    
    curr = pd.merge(curr, standings, on=["Team"]) 
    curr = pd.merge(curr, voting, on=["Player", "Team"], how="outer")
    curr["Share"].fillna(0, inplace=True)
    curr.insert(0, "Season", year)
    output = pd.concat([output, curr], ignore_index=True)

    year += 1

output.to_csv("data.csv", index=False)
