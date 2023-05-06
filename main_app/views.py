from django.shortcuts import render
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect

def home(request):
    response=requests.get('https://mhw-db.com/monsters/2').json()
    all_monsters=requests.get('https://mhw-db.com/monsters').json()
    return render(request, 'home.html', {'monster_1': response, 'all_monsters': all_monsters})

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid Hunter Regisration Info - try again'
    
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
