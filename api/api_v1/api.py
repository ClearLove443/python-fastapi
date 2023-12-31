from fastapi import APIRouter

from api.api_v1.endpoints import demo

api_router = APIRouter()
api_router.include_router(demo.router, tags=["demo"])
