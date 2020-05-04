from django.shortcuts import render, redirect
from django.db import models
from .models import Poem
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User



# Create your views here.
# from django.http import HttpResponse

# Define the home view
# def home(request):
#   return HttpResponse('<h1>home page</h1>')

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def poems_index(request):
  poems = Poem.objects.filter(user=request.user)
  
  return render(request, 'poems/index.html', { 'poems': poems })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

@login_required
def poems_detail(request, poem_id):
  poem = Poem.objects.get(id=poem_id)
  return render(request, 'poems/detail.html', { 'poem': poem })

class PoeCreate(LoginRequiredMixin, CreateView):
  model = Poem
  fields = ['title', 'poem']   #make author value default to the user that made the post
  success_url = '/poems/'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class PoeUpdate(LoginRequiredMixin, UpdateView):
  model = Poem
  fields = ['title', 'poem']
  

class PoeDelete(LoginRequiredMixin, DeleteView):
  model = Poem
  success_url = '/poems/'  