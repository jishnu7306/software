from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),


    

    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard),
    
]
