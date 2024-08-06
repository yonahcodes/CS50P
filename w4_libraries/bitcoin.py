import json
import requests
import sys

def main():
    bitcoins = get_n_of_bitcoins()
    rate = get_rate()
    print(bitcoin_cost(bitcoins, rate))


def bitcoin_cost(n, rate):
    cost = n * rate
    return f"${cost:,.4f}"


def get_rate():
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        r_json = r.json()
        return r_json["bpi"]["USD"]["rate_float"]

    except requests.RequestException:
        sys.exit("Error with file")


def get_n_of_bitcoins():
    try:
        # Get n of bitcoins in command-line argument and convert to float
        bitcoins = float(sys.argv[1])
        return bitcoins
    except IndexError:
        sys.exit("Missing command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")


if __name__ == "__main__":
    main()
