from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .router import app_router

app = FastAPI(title='RecipeInJar')

origins = [
    "http://localhost:3030"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PATCH", "DELETE", "OPTIONS"],
    allow_headers=[
        "Content-Type", "Set-Cookie", 
        "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
        "Authorization"
    ]
)

app.include_router(app_router)
