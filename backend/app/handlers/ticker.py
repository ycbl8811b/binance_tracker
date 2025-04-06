def get_price(ticker: dict) -> float:
    return float(ticker['price'])

def get_symbol(ticker: dict) -> str:
    return ticker['symbol']
