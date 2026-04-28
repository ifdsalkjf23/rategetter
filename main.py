import requests
import json

url = "https://query1.finance.yahoo.com/v7/finance/quote?symbols=USDJPY=X"

res = requests.get(url, timeout=10)
res.raise_for_status()

data = res.json()

results = data.get("quoteResponse", {}).get("result", [])

if not results:
    print("データ取得失敗：resultが空")
else:
    quote = results[0]

    result = {
        "Bid": quote.get("bid"),
        "Ask": quote.get("ask"),
        "Change": quote.get("regularMarketChange")
    }

    print(json.dumps(result, indent=2))
