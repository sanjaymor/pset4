import requests
from sys import argv, exit

if len(argv) != 2:
    exit("Missing command-line argument")

try:
    n = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
except requests.RequestException:
    exit()

data = response.json()

price = float(data["bpi"]["USD"]["rate"].replace(",", ""))

total = n * price

print(f"${total:,.4f}")
