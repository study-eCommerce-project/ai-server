# schemas.py
from pydantic import BaseModel
from typing import List, Optional

class Block(BaseModel):
    type: str                # "text" | "image"
    content: Optional[str] = None
    url: Optional[str] = None

class ProductIn(BaseModel):
    name: str
    price: Optional[int] = None
    options: Optional[str] = None
    category_path: Optional[str] = None
    image_urls: List[str]

class DescriptionOut(BaseModel):
    blocks: List[Block]
