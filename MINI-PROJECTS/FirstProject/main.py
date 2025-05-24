#Тема Робота з БД
# pip install sqlalchemy - встановить sqlalchemy
# pip install sqlite - встановить sqlite
from fastapi import FastAPI, HTTPException, Path, Query, Body, Depends # type: ignore
from typing import Optional, List, Dict, Annotated
from sqlalchemy.orm import Session

from models import User, Post, Base # Імпортуємо моделі з файлу models.py
from database import SessionLocal, engine # Імпортуємо сесію та двигун з файлу database.py
from schemas import UserCreate, PostCreate,User as DBUser, PostResponse # Імпортуємо схеми для валідації даних

app = FastAPI()

Base.metadata.create_all(bind=engine)  # Створюємо таблиці в базі даних

def get_db(): # Функція для отримання сесії бази даних
    db = SessionLocal() # Створюємо нову сесію для роботи з базою даних
    try:
        yield db # Повертаємо сесію для використання в запитах
    finally:
        db.close() # Закриваємо сесію після завершення роботи

@app.post("/users/", response_model=DBUser) # Маршрут для створення нового користувача
async def create_user(user: UserCreate, db: Session = Depends(get_db)) -> User:
    db_user = User(name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

@app.post("/posts/", response_model=PostResponse) # Маршрут для створення нового користувача
async def create_post(post: PostCreate, db: Session = Depends(get_db)) -> Post:
    db_user = db.query(User).filter(User.id == post.author_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    db_post = Post(title=post.title, body=post.body, author_id=post.author_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)

    return db_post

@app.get("/posts/", response_model=List[PostResponse]) # Маршрут для отримання всіх постів
async def get_posts(db: Session = Depends(get_db)) -> List[Post]:
    return db.query(Post).all()