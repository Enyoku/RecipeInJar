from fastapi import APIRouter

from tags.category.router import categories_router
from tags.cuisine.router import cuisine_router

tags_router = APIRouter(prefix="/tag")

tags_router.include_router(categories_router)
tags_router.include_router(cuisine_router)
