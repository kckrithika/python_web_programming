from login.models.User import User as UserModel
def register(username, password):
	user = UserModel(_username = username, _password = password)
	user.save()
	return "OK"