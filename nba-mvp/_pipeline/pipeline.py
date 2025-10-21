import pandas as pd
from utils.per_game.per_game_scraper import fetch_per_game
from utils.advanced.advanced_scraper import fetch_advanced


def pipeline(year_from=1980, year_to=2025):
    per_game = fetch_per_game(year_from=year_from, year_to=year_to)
    advanced = fetch_advanced(year_from=year_from, year_to=year_to)

    return per_game, advanced
