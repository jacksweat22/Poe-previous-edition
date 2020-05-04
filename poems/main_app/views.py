from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from .models import Poems

# Create your views here.
# from django.http import HttpResponse

# Define the home view
# def home(request):
#   return HttpResponse('<h1>home page</h1>')

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def index(request):
  return render(request, 'index.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class PoeCreate(CreateView):
  model = Poems
  fields = ['title', 'poem'] 

class PoeCreate(CreateView):
  model = Poems
  fields = ['title', 'poem']  
  success_url = '/index/'