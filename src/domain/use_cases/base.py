from dependency_injector.wiring import inject, Provide
from sinorstack.exceptions import AppException


class BaseUseCase:
	@inject
	def __init__(self, repo=Provide["repo"]):
		self.repo = repo


	def handle(self, *args, **kwargs):
		raise NotImplementedError

	def execute(self, *args, **kwargs):
		try:
			return self.handle(*args, **kwargs)
		except AppException as e:
			return e.to_dict()