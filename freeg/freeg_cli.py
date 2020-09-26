import argparse
import webbrowser

import colorama
from colorama import Fore

from . import scraper


def print_data(data) :
    for num, i in enumerate(data, start=1) :
        title = Fore.BLUE + i["title"]
        store = Fore.YELLOW + i["store"]

        print(f"{num}. {title} - {store}")


def open_browser(master_list, inputs_list) :

    inputs_list = inputs_list.replace(" ", "").split(",") # remove all spaces then split all choices

    for num_choice in inputs_list :
        if "-" in num_choice :
            start, end = num_choice.split("-")

            slicing = slice(int(start)-1, int(end))
            sliced_games = master_list[slicing]
            [webbrowser.open_new_tab(game["url"]) for game in sliced_games]

        else :
            webbrowser.open_new_tab(master_list[int(num_choice) - 1]["url"])

def main() :
    colorama.init(autoreset=True)

    parser = argparse.ArgumentParser(description="Scrape and show limited free games")

    parser.add_argument("-v", "--view-only", action="store_true", help="List the games without waiting for input to open website")
    parser.add_argument("-tp", "--twitch-prime",action="store_true", help="Show twitch prime/prime gaming limited free games")

    args = parser.parse_args()

    free_games = scraper.extract()
    free_games = sorted(free_games, key=lambda x : x["store"])

    if args.twitch_prime == False :
        free_games = [i for i in free_games if i["store"] != "amazon.com"]

    print_data(free_games)

    if args.view_only == False:
        input_choice = input("\nChoose game(s) :")
        open_browser(free_games, input_choice)

if __name__ == "__main__":
    main()