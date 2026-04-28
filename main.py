import requests
import json

# 名古屋の座標
url = "https://api.open-meteo.com/v1/forecast?latitude=35.1815&longitude=136.9066&current_weather=true"

try:
    print("リクエスト送信中...")
    
    res = requests.get(url, timeout=10)
    res.raise_for_status()

    print("レスポンス受信OK")

    data = res.json()
    current = data.get("current_weather", {})

    result = {
        "気温": current.get("temperature"),
        "風速": current.get("windspeed"),
        "風向": current.get("winddirection"),
        "天気コード": current.get("weathercode"),
        "取得時刻": current.get("time")
    }

    print("取得結果👇")
    print(json.dumps(result, indent=2, ensure_ascii=False))

except Exception as e:
    print("エラー発生:", e)
