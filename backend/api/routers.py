from fastapi import APIRouter

from api.recipes.router import recipe_router
from api.users.router import account_router

app_router = APIRouter()

app_router.include_router(recipe_router)
app_router.include_router(account_router)
