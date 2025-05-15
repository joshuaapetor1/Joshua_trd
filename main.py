from mt5_setup import initialize_mt5, open_trade, shutdown_mt5
from telegram_alert import send_alert
from utils import log_to_google_sheets

account = 12345678
password = 'your_password'
server = 'Exness-MT5Real'

initialize_mt5(account, password, server)

symbol = 'EURUSD'
volume = 0.1

result = open_trade(symbol, volume, order_type='buy')
profit = result.profit if hasattr(result, 'profit') else 0.0

log_to_google_sheets(profit)
send_alert(f"Executed {symbol} trade. Profit: {profit:.2f} USD")

shutdown_mt5()