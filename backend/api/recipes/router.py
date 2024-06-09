from fastapi import APIRouter

from recipes.tags.routers import tags_router
from recipes.posts.router import posts_router

recipe_router = APIRouter(prefix="/recipes", tags=["Recipe",])

recipe_router.include_router(tags_router)
recipe_router.include_router(posts_router)
