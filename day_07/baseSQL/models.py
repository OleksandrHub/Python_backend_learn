# опис таблиці база даних
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship # зв'язок між таблицями
from database import Base # підключення бази

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True) # первинний ключ
    name = Column(String, index=True) # ім'я користувача
    age = Column(Integer) # вік користувача

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True) # первинний ключ
    title = Column(String, index=True) # заголовок s
    body = Column(String) # тіло поста
    author_id = Column(Integer, ForeignKey('users.id')) # зовнішній ключ на таблицю користувачів

    author = relationship("User") # зв'язок з таблицею користувачів