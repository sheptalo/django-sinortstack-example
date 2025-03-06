from rest_framework.decorators import api_view
from rest_framework.response import Response
from src.entrypoint import main

container = main()


@api_view(["POST"])
def register(request):
    result = container.controllers.register_user().execute(request.data)
    return Response(result, status=result.pop("status_code", 200))
