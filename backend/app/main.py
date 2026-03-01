"""FastAPI application entry point.

Creates the Chimera Dungeon backend server with CORS middleware,
lifespan management, and the /api/health endpoint.
"""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan: startup and shutdown hooks."""
    logging.basicConfig(level=settings.log_level)
    logger.info(
        "Chimera Dungeon starting (env=%s, tick_rate=%dHz)",
        settings.environment,
        settings.tick_rate,
    )
    yield
    logger.info("Chimera Dungeon shutting down")


app = FastAPI(
    title="Chimera Dungeon",
    lifespan=lifespan,
)

# CORS middleware -- origins parsed from comma-separated env var
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint."""
    return {"status": "ok"}
