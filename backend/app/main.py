from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from services.market_service import market_service
import asyncio

app = FastAPI()

@app.on_event("startup")
def startup():
    asyncio.create_task(market_service.start())

@app.get('/stream-tickers')
async def stream_tickers():
    """ SSE-stream for frontend """
    async def event_generator():
        async for data in market_service.subscribe():
            yield f"{data}\n\n"

    return StreamingResponse(
        event_generator(),
        media_type="text/event-stream"
    )
