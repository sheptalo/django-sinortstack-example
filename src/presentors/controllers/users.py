from sinorstack.controllers import BaseController

from src.domain.user import User


class RegisterUserController(BaseController):
    def handle(self, validated_data):
        user = User.from_dict(validated_data)
        new_user = self.use_case.execute(user)
        return new_user.to_dict
