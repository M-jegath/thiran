from __future__ import annotations

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1.routers.health import router as health_router
from app.db.session import Base, engine


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, debug=settings.debug)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.backend_cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.on_event("startup")
    def on_startup() -> None:
        # Create database tables on startup (simple dev approach)
        Base.metadata.create_all(bind=engine)

    app.include_router(health_router, prefix=settings.api_v1_prefix)

    @app.get("/")
    def root():
        return {"name": settings.app_name}

    return app


app = create_app()
