from django.http import HttpResponse
from login.controllers import User as UserController
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def register(request):
	params = request.POST #request.body
	print(params)
	username = params['username']
	print(username)
	password = params['password']
	print(password)
	result = UserController.register(username, password)
	return HttpResponse(result, status=200)