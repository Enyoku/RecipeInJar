from datetime import datetime

from pydantic import BaseModel
from PIL import Image

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
    img: Image
    bio: str
    is_verified: bool
    is_staff: Image
    created_on: datetime

