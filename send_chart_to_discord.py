import billboard
import requests

# Billboard HOT 100チャート取得
chart = billboard.ChartData('hot-100')

# 上位10曲のリストを作成
message = "**Billboard HOT 100 Top 10**\n"
for i in range(20):
    entry = chart[i]
    message += f"{i + 1}. {entry.title} - {entry.artist}\n"

# Discord Webhook URL（自分のWebhookに置き換える）
WEBHOOK_URL = 'https://discordapp.com/api/webhooks/1368973300939751584/PkoOylb8HYY0ltxlJLEY-4XK2LI-wOtJXdDC8Fq_r_lNC9r3iuWEyOdhZ9L1_fwZjJnL'

# Discordに送信
payload = {"content": message}
response = requests.post(WEBHOOK_URL, json=payload)

if response.status_code == 204:
    print("送信成功！")
else:
    print(f"送信失敗: {response.status_code}, {response.text}")
