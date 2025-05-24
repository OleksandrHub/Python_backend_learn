#Тема: Обробка url-адрес та робота з параметрами запиту
#pip install fastapi - встановить fastapi
#pip install uvicorn - встановить uvicorn
#uvicorn main:app --reload - запустить сервер
from fastapi import FastAPI # FastAPI - це фреймворк для створення API

app = FastAPI() # створюємо екземпляр FastAPI

@app.get("/") # декоратор для визначення маршруту
def home():
    return "Hello, World!" # повертаємо JSON-об'єкт з повідомленням
