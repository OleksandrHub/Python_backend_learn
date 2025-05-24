from pydantic import BaseModel, Field
# User schemas
class UserBase(BaseModel):
    name: str
    age: int

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
    
class UserCreate(UserBase):
    pass
# Post schemas
class PostBase(BaseModel):
    title: str
    body: str
    author_id: int

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    id: int
    author: User

    class Config:
        orm_mode = True