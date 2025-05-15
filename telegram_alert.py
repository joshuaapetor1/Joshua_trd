import telepot

TELEGRAM_BOT_TOKEN = "your_bot_token"
TELEGRAM_USER_ID = 123456789  # Replace with your Telegram ID

bot = telepot.Bot(TELEGRAM_BOT_TOKEN)

def send_alert(message):
    try:
        bot.sendMessage(TELEGRAM_USER_ID, message)
    except Exception as e:
        print("Telegram Error:", e)