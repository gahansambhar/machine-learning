from bs4 import BeautifulSoup
import pandas as pd
import requests
import time


def fetch_per_game(year_from=1980, year_to=2025):
    year = year_from

    df = pd.DataFrame()
    while year <= year_to:

        # Extracting HTML content from required basketball reference page
        url = f"https://www.basketball-reference.com/leagues/NBA_{year}_per_game.html"
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")

        # Finding the player stats table
        table = soup.find_all("table")[0]

        # Grabbing the headers for the table
        headers = table.find_all("th")
        headers = [header.text for header in headers]

        s = headers.index("Rk")
        e = headers.index("Awards")

        headers = headers[s : e + 1]

        # Creating the dataframe to store the data
        curr = pd.DataFrame(columns=headers)

        # Processing each row individually and adding them to the dataframe
        rows = table.find_all("tr")
        currsize = 0

        for row in rows:
            rowdata = []

            for cell in row:
                rowdata.append(cell.text.strip())

            rowdata = [rowdata[i] for i in range(len(rowdata)) if i % 2 == 1]

            if rowdata[0] != "Rk" and rowdata[0] != "":
                curr.loc[currsize] = rowdata
                currsize += 1
        curr.insert(0, "year", year)
        year += 1
        df = pd.concat([df, curr])
        time.sleep(1)

    return df
