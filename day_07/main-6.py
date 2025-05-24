from fastapi import FastAPI, HTTPException, Path, Query, Body # type: ignore # бібліотека FastAPI для створення веб-додатків
from typing import Optional, List, Dict, Annotated # бібліотека для роботи з типами даних
from pydantic import BaseModel, Field

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

class PostCreate(BaseModel): # створюємо модель даних для створення постів
    title: str
    body: str
    author_id: int

class UserCreate(BaseModel): # створюємо модель даних для створення користувачів
    name: Annotated[str, Field(..., title="Ім'я користувача" ,min_length=3, max_length=50)] # обмеження на довжину імені
    age: Annotated[int, Field(..., title="Вік користувача", ge=18, le=100)] # обмеження на вік користувача

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

@app.post("items/add")
async def add_item(post: PostCreate) -> Post: # створюємо маршрут для додавання нового поста
    author = next((user for user in users if user["id"] == post.author_id), None)
    if not author:
        raise HTTPException(status_code=404, detail="Author not found")
    
    new_post_id = len(posts) + 1
    new_post = {"id": new_post_id, "title": post.title, "body": post.body, "author": author}

    posts.append(new_post)
    return Post(**new_post) # повертаємо новий пост

@app.post("user/add")
async def add_user(user: Annotated[UserCreate, Body(...,example = {"name": "John", "age": 31} , embed=True)]) -> User: # створюємо маршрут для додавання нового користувача(post: PostCreate) -> Post: # створюємо маршрут для додавання нового поста
    new_user_id = len(users) + 1
    new_user = {"id": new_user_id, "name": user.name, "age": user.age}

    users.append(new_user)
    return Post(**new_user)

#@app.put("/items/{id}") http запит для оновлення поста
#@app.delete("/items/{id}") # http запит для видалення поста

@app.get("/items/{id}")
async def items(id: Annotated[int, Path(..., title="Задає id поста", ge=1, lt=100)]) -> Post: # створюємо маршрут для отримання поста за id, path - динамічні параметри
    for post in posts:
        if post["id"] == id:
            return Post(**post)
    
    raise HTTPException(status_code=404, detail="POST not found") # якщо не знайдено, то повертаємо помилку 404


@app.get("/search")
async def search(post_id: Annotated[Optional[int], Query(title="ID post to search", ge=1, le = 50)]) -> Dict[str, Optional[Post]]: # створюємо маршрут для пошуку постів за id, qurey - параметри запиту
    if post_id:
        for post in posts:
            if post["id"] == post_id:
                return {"data": Post(**post)}
            
        raise HTTPException(status_code=404, detail="POST not found")
    else:
        return {"data": None}