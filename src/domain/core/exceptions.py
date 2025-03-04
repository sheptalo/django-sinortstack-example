from sinorstack.exceptions import AppException



class ValidationError(AppException):
	message = "Ошибка валидации"
	status_code = 422

	def __init__(self, errors):
		self.message = errors