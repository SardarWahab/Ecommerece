
from django.contrib import admin
from django.urls import path
from home.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('get_product/', get_product,name='get_product'),
    path('save_product/',save_product,name='save_product'),
    path('delete_product/<int:id>/',delete_product,name='delete_product'),
    path('get_product/<int:id>/',get_single_product,name='get_single_product'),


]
