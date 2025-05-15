import MetaTrader5 as mt5

def initialize_mt5(account, password, server):
    if not mt5.initialize(login=account, password=password, server=server):
        raise RuntimeError("MT5 Initialization failed: ", mt5.last_error())
    print("MT5 initialized")

def shutdown_mt5():
    mt5.shutdown()

def open_trade(symbol, volume, order_type='buy'):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None or not symbol_info.visible:
        mt5.symbol_select(symbol, True)

    point = symbol_info.point
    price = mt5.symbol_info_tick(symbol).ask if order_type == 'buy' else mt5.symbol_info_tick(symbol).bid
    deviation = 20

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": mt5.ORDER_TYPE_BUY if order_type == 'buy' else mt5.ORDER_TYPE_SELL,
        "price": price,
        "deviation": deviation,
        "magic": 123456,
        "comment": "Arbitrage Bot",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_IOC,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        print(f"Order failed: {result.retcode}")
    else:
        print(f"Trade executed: {result}")
    return result