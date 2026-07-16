import requests, sys

URL = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey=7e3906063c4ba25d6d7b3bb7403ac02ca7ed810facec9d7e8a9e3b8c1e8e6fa2"


def main():
    validate_arguments(sys.argv)

    bitcoins = get_bitcoins_float(sys.argv[1])

    content = get_response()

    usd = get_usd(content) * bitcoins

    print(f"${usd:,.4f}")


def validate_arguments(arguments):
    if len(arguments) != 2:
        sys.exit("Missing command-line argument")


def get_bitcoins_float(bitcoins):
    try:
        return float(bitcoins)
    except ValueError:
        sys.exit("Command-line argument is not a number")


def get_response():
    try:
        response = requests.get(URL)
    except requests.RequestException as e:
        sys.exit(e)

    return response.json()


def get_usd(content):
    try:
        return float(content.get("data").get("priceUsd"))
    except ValueError:
        sys.exit("Invalid usd price response")


if __name__ == "__main__":
    main()
