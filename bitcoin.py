import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response.raise_for_status()
except requests.RequestException:
    sys.exit()

data = response.json()
price = data["bpi"]["USD"]["rate_float"]

print(f"${n * price:,.4f}")
