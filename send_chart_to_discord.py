import billboard
import requests

# Billboard HOT 100チャート取得
chart = billboard.ChartData('hot-100')

# 上位20曲のリストを作成
message = "**Billboard HOT 100 Top 20**\n"
for i in range(20):
    entry = chart[i]
    message += f"{i + 1}. {entry.title} - {entry.artist}\n"

# Discord Webhook URL（自分のWebhookに置き換える）
WEBHOOK_URL = 'https://discord.com/api/webhooks/ここにあなたのWebhook'

# Discordに送信
payload = {"content": message}
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("送信成功！")
else:
    print(f"送信失敗: {response.status_code}, {response.text}")
