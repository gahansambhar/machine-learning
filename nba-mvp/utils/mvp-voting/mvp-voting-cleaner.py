import pandas as pd

year = 1980

while year <= 2025:
    file = f"{year-1}-{year}-mvp-voting.csv"
    df = pd.read_csv(file)
    headers = df.columns
    to_drop = [h for h in headers if h not in ["Player", "Tm", "Share"]]
    df = df.drop(to_drop, axis=1)
    df.to_csv(file, index=False)
    year += 1
