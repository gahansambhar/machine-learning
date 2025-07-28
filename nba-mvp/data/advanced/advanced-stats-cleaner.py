import pandas as pd

year = 1980

while year <= 2025:
    file = f"{year-1}-{year}-advanced-stats.csv"
    df = pd.read_csv(file)

    df = df[~df['Team'].isin(["2TM", "3TM", "4TM", "5TM"])]
    df.to_csv(file, index=False)
    year += 1
