from .base import BaseUseCase


class RegisterUserUseCase(BaseUseCase):
	def handle(self, user, *args, **kwargs):
		user.hash_password()
		return self.repo.create(user)