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

def large_monsters(request):
    large_monsters=requests.get('https://mhw-db.com/monsters?q={"type":"large"}').json()
    return render(request, 'large_monsters.html', {'large_monsters': large_monsters})

def small_monsters(request):
    small_monsters=requests.get('https://mhw-db.com/monsters?q={"type":"small"}').json()
    return render(request, 'small_monsters.html', {'small_monsters': small_monsters})

def monster_detail(request, monster_name):
    url = f'https://mhw-db.com/monsters?q={{"name":"{monster_name}"}}'
    monster = requests.get(url).json()[0]
    return render(request, 'monster_detail.html', {'monster': monster})

def material_list(request):
    pass