import billboard
import requests

chart = billboard.ChartData('hot-100')
message = "**Billboard HOT 100 Top 5**\n"
for i in range(5):
    entry = chart[i]
    message += f"{i + 1}. {entry.title} - {entry.artist}\n"

WEBHOOK_URL = 'あなたのWebhook_URLをここに貼る'

payload = { "content": message }
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("送信成功！")
else:
    print(f"送信失敗: {response.status_code}, {response.text}")
