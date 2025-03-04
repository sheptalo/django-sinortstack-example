from sinorstack.drf.decorators import inject_controller
from rest_framework.response import Response

from config.containers import ApplicationContainer


@inject_controller(ApplicationContainer.controllers.register_user, ['POST'])
def register(request, controller):
	result = controller.execute(request.data)
	return Response(result, status=result.pop('status_code', 200))