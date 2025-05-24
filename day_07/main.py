#Тема: Використання бібліотеки Pydantic для валідації даних
#pip install fastapi - встановить fastapi
#pip install uvicorn - встановить uvicorn
#uvicorn main:app --reload - запустить сервер
from fastapi import FastAPI, HTTPException # FastAPI - це фреймворк для створення API
from typing import Optional, List, Dict # Optional - це тип, який дозволяє вказати, що параметр може бути відсутнім 
from pydantic import BaseModel # BaseModel - це клас, який дозволяє створювати моделі даних

app = FastAPI() # створюємо екземпляр FastAPI

class User(BaseModel): # створюємо модель даних
    id: int
    name: str
    age: int

class Post(BaseModel): # створюємо модель даних
    id: int
    title: str
    body: str
    author: User # модель даних для постів, яка містить автора


users = [
    {"id": 1, "name": "John", "age": 31},
    {"id": 2, "name": "Jane", "age": 23},
    {"id": 3, "name": "Doe", "age": 39},
]    

posts = [
    {"id": 1, "title": "News 1", "body": "Content of post 1", 'author': users[1]}, 
    {"id": 2, "title": "News 2", "body": "Content of post 2", 'author': users[0]},
    {"id": 3, "title": "News 3", "body": "Content of post 3", "author": users[2]},
]

 
# async def items() -> List[Post]: # створюємо маршрут для отримання всіх постів
#     post_objects = []
#     for post in posts:
#         post_objects.append(Post(id=post["id"], title=post["title"], body=post["body"]))
#     return post_objects
@app.get("/items")
async def items() -> List[Post]: # створюємо маршрут для отримання всіх постів
    return [Post(**post) for post in posts]

@app.get("/items/{id}")
async def items(id: int) -> Post: # створюємо маршрут для отримання поста за id
    for post in posts:
        if post["id"] == id:
            return Post(**post)
    
    raise HTTPException(status_code=404, detail="POST not found") # якщо не знайдено, то повертаємо помилку 404
    
@app.get("/search")
async def search(post_id: Optional[int] = None) -> Dict[str, Optional[Post]]: # створюємо маршрут для пошуку постів за id
    if post_id:
        for post in posts:
            if post["id"] == post_id:
                return {"data": Post(**post)}
            
        raise HTTPException(status_code=404, detail="POST not found")
    else:
        return {"data": None}

