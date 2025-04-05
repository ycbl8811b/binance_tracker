from binance.client import Client

client = Client()

tickers = client.get_all_tickers()
print(tickers)
for ticker in tickers:
    print(f"{ticker['symbol']}:{ticker['price']}")


btc_info = client.get_symbol_info('BTCUSDT')
print(btc_info)

