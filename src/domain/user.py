from dataclasses import dataclass

from src.application import settings
from src.domain.base import BaseEntity
from src.application.exceptions import ValidationError


@dataclass
class User(BaseEntity):
    username: str
    password: str

    @classmethod
    def validate(cls, d):
        if not d.get("username") or not d.get("password"):
            raise ValidationError(
                {"username": ["cannot be empty"], "password": ["cannot be empty"]}
            )

    def hash_password(self):
        import hashlib
        import hmac

        secret_key = hashlib.sha256(settings.SECRET_KEY.encode("utf-8")).digest()
        self.password = hmac.new(
            secret_key,
            self.password.encode("utf-8"),
            hashlib.sha256,
        ).hexdigest()
