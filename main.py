from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from core.config import settings
from core.schemas import db_helper, Base


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # shutdown
    print('Closing DB connection')
    await db_helper.dispose()


app = FastAPI(
    lifespan=lifespan,
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.run.host, port=settings.run.port, reload=True)
