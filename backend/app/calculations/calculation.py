from handlers.ticker import get_price

def sum_tickers(*tickers: list) -> float:
    res = get_price(tickers[0])
    for ticker in tickers[1:]:
        res += get_price(ticker)
    return res


def subdivide_tickers(*tickers: list) -> float:
    res = get_price(tickers[0])
    for ticker in tickers[1:]:
       res -= get_price(ticker)
    return res


def multiply_tickers(*tickers: list) -> float:
    res = get_price(tickers[0])
    for ticker in tickers[1:]:
        res *= get_price(ticker)
    return res


def divide_tickers(*tickers: list) -> float:
    res = get_price(tickers[0])
    for ticker in tickers[1:]:
        res /= get_price(ticker)
    return res
