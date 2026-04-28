import requests
import json
from datetime import datetime

# 名古屋の座標
url = "https://api.open-meteo.com/v1/forecast?latitude=35.1815&longitude=136.9066&current_weather=true"

try:
    print("リクエスト送信中...")

    res = requests.get(url, timeout=10)
    res.raise_for_status()

    print("レスポンス受信OK")

    data = res.json()
    current = data.get("current_weather", {})

    if not current:
        print("データがありません")
    else:
        result = {
            "気温": current.get("temperature"),
            "風速": current.get("windspeed"),
            "風向": current.get("winddirection"),
            "天気コード": current.get("weathercode"),
            "取得時刻": current.get("time")
        }

        # ログを表示
        print("取得結果👇")
        print(json.dumps(result, indent=2, ensure_ascii=False))
        
        # ファイルに追記
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"{now} - 気温: {result['気温']}°C, 風速: {result['風速']} m/s, 風向: {result['風向']}°, 天気コード: {result['天気コード']}, 取得時刻: {result['取得時刻']}\n"
        
        with open('weather_history.txt', 'a', encoding='utf-8') as f:
            f.write(log_line)

        print("データをファイルに記録しました")

except requests.exceptions.RequestException as e:
    print("リクエストエラー:", e)
except Exception as e:
    print("その他のエラー:", e)
