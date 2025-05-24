from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQL_DB_URL = "sqlite:///./sql_app.db" # URL для підключення до бази даних SQLite

engine = create_engine(SQL_DB_URL, connect_args={"check_same_thread": False}) # створюємо з'єднання з базою даних SQLite

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # створюємо сесію для роботи з БД

Base = declarative_base() # створюємо базовий клас для моделей