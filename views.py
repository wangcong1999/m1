from django.http import HttpResponse


def index(request):
	return HttpResponse('index')


def login(request):
	return HttpResponse('login')
