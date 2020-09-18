import webbrowser
import argparse
from . import scraper

def print_data(data) :
    for num, i in enumerate(data, start=1) :
        numerate_title = "{0}. {1} - {2}".format(num, i["title"], i["store"])
        print(numerate_title)


def main() :
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
        num = int(input()) - 1 # used to choose game. minus one because variable free_games is list, and list index start from zero.
        webbrowser.open_new_tab(free_games[num]["link"])

if __name__ == "__main__":
    main()