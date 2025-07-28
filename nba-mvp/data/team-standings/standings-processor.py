import pandas as pd


def record_to_pct(record):
    """
    Convert a win-loss record string to a win percentage.

    Parameters:
        record (str): A string representing the team's record in the format 'W-L',
                      where W is the number of wins and L is the number of losses.

    Returns:
        float: The win percentage as a float rounded to two decimal places (e.g., 73.65 for 73.65%).
    """
    W, L = record.split("-")
    W, L = int(W), int(L)
    return round(W / (W + L) * 100, 2)


year = 1980


while year <= 2025:
    file = f"{year-1}-{year}-team-standings.csv"
    df = pd.read_csv(file)
    for col in df.columns[2:]:
        df[col] = df[col].apply(record_to_pct)
    df.to_csv(file, index=False)
    year += 1
