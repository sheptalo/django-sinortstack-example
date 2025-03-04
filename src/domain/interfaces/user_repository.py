from abc import ABC, abstractmethod

from domain.user import User


class UserRepository(ABC):
    @abstractmethod
    def get(self, username: str) -> User:
        pass

    @abstractmethod
    def create(self, user: User) -> User:
        pass
