import requests

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=USDJPY=X"

res = requests.get(url, timeout=10)
res.raise_for_status()

data = res.json()
quote = data["quoteResponse"]["result"][0]

result = {
    "Bid": quote.get("bid"),
    "Ask": quote.get("ask"),
    "Change": quote.get("regularMarketChange")
}

print(result)
