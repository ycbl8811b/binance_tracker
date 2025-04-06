from binance import AsyncClient, BinanceSocketManager
from collections import defaultdict
import asyncio

class MarketService:
    def __init__(self):
        self.client = None
        self.bm = None
        self.last_tickers = dict()
        self.subscribers = set()

    async def start(self):
        self.client = await AsyncClient.create()
        self.bm = BinanceSocketManager(self.client)
        
        ts = self.bm.ticker_socket()
        async with ts as tscm:
            while True:
                msg = await tscm.recv()
                await self.handle_all_tickers(msg)


    async def handle_all_tickers(self, msg):
        for ticker in msg:
            symbol = ticker['s']
            self.last_tickers[symbol] = ticker['p']

        # Notify subscribers
        for queue in self.subscribers:
            await queue.put(self.last_tickers.copy())


    async def subscribe(self):
        """ Subscribe to updates (SSE)"""
        queue = asyncio.Queue()
        self.subscribers.add(queue)
        try:
            while True:
                yield await queue.get()
        finally:
            self.subscribers.remove(queue)

market_service = MarketService()
