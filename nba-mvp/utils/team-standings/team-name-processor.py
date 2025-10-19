import pandas as pd
team_name_to_code = {
    "Atlanta Hawks": "ATL",
    "Boston Celtics": "BOS",
    "Brooklyn Nets": "BRK",
    "Charlotte Hornets": "CHO",
    "Chicago Bulls": "CHI",
    "Cleveland Cavaliers": "CLE",
    "Dallas Mavericks": "DAL",
    "Denver Nuggets": "DEN",
    "Detroit Pistons": "DET",
    "Golden State Warriors": "GSW",
    "Houston Rockets": "HOU",
    "Indiana Pacers": "IND",
    "Los Angeles Clippers": "LAC",
    "Los Angeles Lakers": "LAL",
    "Memphis Grizzlies": "MEM",
    "Miami Heat": "MIA",
    "Milwaukee Bucks": "MIL",
    "Minnesota Timberwolves": "MIN",
    "New Orleans Pelicans": "NOP",
    "New York Knicks": "NYK",
    "Oklahoma City Thunder": "OKC",
    "Orlando Magic": "ORL",
    "Philadelphia 76ers": "PHI",
    "Phoenix Suns": "PHO",
    "Portland Trail Blazers": "POR",
    "Sacramento Kings": "SAC",
    "San Antonio Spurs": "SAS",
    "Toronto Raptors": "TOR",
    "Utah Jazz": "UTA",
    "Washington Wizards": "WAS",
    "New Jersey Nets": "NJN",
    "Seattle SuperSonics": "SEA",
    "Vancouver Grizzlies": "VAN",
    "Charlotte Bobcats": "CHA",
    "New Orleans Hornets": "NOH",
    "San Diego Clippers": "SDC",
    "Kansas City Kings": "KCK",
    "Washington Bullets": "WSB"
}

year = 1980

while year <= 2025:
    file = f"{year-1}-{year}-team-standings.csv"
    df = pd.read_csv(file)
    df["Team"] = df["Team"].map(team_name_to_code)
    df.to_csv(file, index=False)
    year += 1
