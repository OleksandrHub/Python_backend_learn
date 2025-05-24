#Тема: Обробка url-адрес та робота з параметрами запиту
#pip install fastapi - встановить fastapi
#pip install uvicorn - встановить uvicorn
#uvicorn main:app --reload - запустить сервер
from fastapi import FastAPI, HTTPException # type: ignore # FastAPI - це фреймворк для створення API
from typing import Optional # Optional - це тип, який дозволяє вказати, що параметр може бути відсутнім 

app = FastAPI() # створюємо екземпляр FastAPI

@app.get("/") # декоратор для визначення маршруту
async def home() -> list: # тип даних, які повертає функція це список
    return [1, 5] # повертаємо список з двома числами

@app.get("/contacts")
async def contacts() -> int:
    return 34 # повертаємо ціле число

posts = [
    {"id": 1, "title": "News 1", "body": "Content of post 1"}, 
    {"id": 2, "title": "News 2", "body": "Content of post 2"},
    {"id": 3, "title": "News 3", "body": "Content of post 3"},
]

@app.get("/items")
async def items() -> list:
    return posts

@app.get("/items/{id}")
async def items(id: int) -> dict:
    for post in posts:
        if post["id"] == id:
            return post
    
    raise HTTPException(status_code=404, detail="POST not found") # якщо не знайдено, то повертаємо помилку 404
    
@app.get("/search")
async def search(post_id: Optional[int] = None) -> dict:
    if post_id:
        for post in posts:
            if post["id"] == post_id:
                return post
            
        raise HTTPException(status_code=404, detail="POST not found")
    else:
        return {"data": "No post ID provided"}

