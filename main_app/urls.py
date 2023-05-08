from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('large_monsters/', views.large_monsters, name='large_monsters'),
    path('small_monsters/', views.small_monsters, name='small_monsters'),
    path('monster/<str:monster_name>', views.monster_detail, name='monster_detail'),
    path('material_list', views.material_list, name='material_list'),
    path('material_list_item/create', views.Material_List_ItemCreate.as_view(), name='material_list_item_create'),
    path('material_list_item/<int:pk>/delete/', views.Material_List_ItemDelete.as_view(), name='material_list_item_delete'),
    path('material_list_item/<int:pk>/update/', views.Material_List_ItemUpdate.as_view(), name='material_list_item_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])