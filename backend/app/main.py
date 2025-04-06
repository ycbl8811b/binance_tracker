import asyncio
from binance.async_client import AsyncClient 


from calculations.calculation import (
    sum_tickers, subdivide_tickers,
    multiply_tickers, divide_tickers
)

tickers = None

async def fetch_tickers(client):
    return await client.get_all_tickers()

async def update_tickers(client):
    global tickers
    while True:
        tickers = await fetch_tickers(client)
        print(tickers[0]['symbol'], tickers[0]['price'])
        await asyncio.sleep(1)
    

async def get_user_input():
    global tickers
    while True:
        user_input = await asyncio.to_thread(input, "Smt")
        print("user: m")
        if user_input == "m":
            print(f"[m] {ticker[0]['symbol']}:{ticker[0]['price']}")

async def main():
    client = await AsyncClient().create()
    task_fetch = asyncio.create_task(update_tickers(client))
    # task_input = asyncio.create_task(get_user_input())
    
    #await asyncio.gather(task_fetch, task_input)
    await asyncio.gather(task_fetch)

asyncio.run(main())
