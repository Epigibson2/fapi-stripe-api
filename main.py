from fastapi import FastAPI

from api.v1.router import router
from core.config import settings
from contextlib import asynccontextmanager
from dependencies.database import init_db
from docs import tags_metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB.
    await init_db()
    print("Init db ...")
    yield


app = FastAPI(
    title=settings.PROJECT_NAME,
    description="Stripe API Payments",
    version="0.1.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata,
    docs_url=f"{settings.API_V1_STR}/docs",
    redoc_url=f"{settings.API_V1_STR}/redoc",
    lifespan=lifespan
)

app.include_router(router, prefix=settings.API_V1_STR)
