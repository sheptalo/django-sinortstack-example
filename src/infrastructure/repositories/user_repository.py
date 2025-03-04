from domain.user import User
from domain.interfaces.user_repository import UserRepository

from django.contrib.auth.models import User as DjangoUser
import sqlite3


class DjangoUserRepository(UserRepository):
    def create(self, user: User):
        orm_user = DjangoUser.objects.create(**user.to_dict)
        return User.from_dict(orm_user.__dict__)

    def get(self, username: str) -> User:
        orm_user = DjangoUser.objects.get(username=username)
        return User.from_dict(orm_user.__dict__)


class SQLiteUserRepository(UserRepository):
    def create(self, user: User):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
        """)
        conn.commit()
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?) ",
            (user.username, user.password),
        )
        conn.commit()
        return user

    def get(self, username: str) -> User:
        pass