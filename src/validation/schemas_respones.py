from typing import List, Optional
from pydantic import BaseModel, Field

class Category(BaseModel):
    id: Optional [int]  = None
    name: Optional [str]  = None

class Tag(BaseModel):
    id: Optional [int]  = None
    name: Optional [str]  = None

class FullPetObject(BaseModel):
    id: int
    category: Optional[Category] = None
    name: Optional [str]  = None
    photoUrls: Optional[List[str]] = None
    tags: Optional[List[Tag]] = None
    status: Optional[str] = None
