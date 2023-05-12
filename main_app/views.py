from django.shortcuts import render
import requests
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Material_List_Item, Monster_Image, Small_Monster_Image
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

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
    monster_images = Monster_Image.objects.all()
    return render(request, 'large_monsters.html', {'large_monsters': large_monsters, 'monster_images':monster_images})

def small_monsters(request):
    small_monsters=requests.get('https://mhw-db.com/monsters?q={"type":"small"}').json()
    small_monster_images = Small_Monster_Image.objects.all()
    return render(request, 'small_monsters.html', {'small_monsters': small_monsters, 'small_monster_images': small_monster_images})

def monster_detail(request, monster_name):
    url = f'https://mhw-db.com/monsters?q={{"name":"{monster_name}"}}'
    monster = requests.get(url).json()[0]
    return render(request, 'monster_detail.html', {'monster': monster})

@login_required
def material_list(request):
    user_material_list = Material_List_Item.objects.filter(user=request.user)
    return render(request, 'material_list.html', {'user_material_list':user_material_list})

class Material_List_ItemCreate(LoginRequiredMixin, CreateView):
    model = Material_List_Item
    fields = ['item']
    success_url = '/material_list'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the item
        return super().form_valid(form)
    
class Material_List_ItemDelete(LoginRequiredMixin, DeleteView):
    model = Material_List_Item
    success_url = '/material_list'

class Material_List_ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Material_List_Item
    fields = ['item']
    success_url = '/material_list'
