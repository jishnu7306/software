from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index, name='index'),

    #*************************  client  ****************************
    path('base_client',views.base_client),
    path('client_Dashboard',views.client_Dashboard),
    path('client_project_details',views.client_project_details),
    path('client_company_card',views.client_company_card),
    path('client_company_details1',views.client_company_details1),
    path('client_company_details2',views.client_company_details2),
    path('client_company_details3',views.client_company_details3),





    

    #***************************** Manager ******************************

    path('manager_Dashboard',views.manager_Dashboard),
    
]
