from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


year = 1980
while year <= 2025:

    # Extracting HTML content from required basketball reference page
    url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Finding the player stats table
    table = soup.find_all("table")[0]

    # Grabbing the headers for the table
    headers = table.find_all("th")
    headers = [header.text for header in headers]

    # Finding the indicies of the headeres needed
    s = headers.index("Player")
    e = headers.index("PTS")
    headers = headers[s:e+1]

    # Creating the dataframe to store the data
    df = pd.DataFrame(columns=headers)

    # Processing each row individually and adding them to the dataframe
    rows = table.find_all("tr")
    dfsize = 0

    for row in rows:
        rowdata = []

        for cell in row:
            rowdata.append(cell.text.strip())

        rowdata = [rowdata[i] for i in range(len(rowdata)) if i % 2 == 1]

        if rowdata[0] != "Rk" and rowdata[0] != "":
            df.loc[dfsize] = rowdata[1:-1]
            dfsize += 1

    # Extracting info to a csv
    df.to_csv(f"{year-1}-{year}-per-game-stats.csv")

    year += 1
    time.sleep(5)
