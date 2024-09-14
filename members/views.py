from django.http import HttpResponse
from django.template import loader



def members(request):
  template = loader.get_template('myFirst.html')
  return HttpResponse(template.render())

def myFirst(request):
  template = loader.get_template('myFirst.html')
  return HttpResponse(template.render())

def login(request):
  template = loader.get_template('login.html')
  return HttpResponse(template.render())

def signIn(request):
  template = loader.get_template('signIn.html')
  return HttpResponse(template.render())