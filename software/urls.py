from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
  

    #*************************  client  ****************************
    #path('base_client',views.base_client),
    path('client_Dashboard',views.client_Dashboard),
    path('client_project_card',views.client_project_card),
    path('client_company_card',views.client_company_card),
    path('client_company_details1',views.client_company_details1),
    path('client_company_details2',views.client_company_details2),
    path('client_company_details3',views.client_company_details3),
    path('client_company_details4',views.client_company_details4),
    path('client_company_details5',views.client_company_details5),
    path('client_company_details6',views.client_company_details6),
    path('client_company_details7',views.client_company_details7),
    path('client_company_details8',views.client_company_details8),
    path('client_company_details9',views.client_company_details9),
    path('client_company_details10',views.client_company_details10),
    path('client_project_details1',views.client_project_details1),
    path('client_project_details2',views.client_project_details2),
    path('client_project_details3',views.client_project_details3),
    path('client_project_details4',views.client_project_details4),
    path('client_project_details5',views.client_project_details5),
    path('client_project_details6',views.client_project_details6),
    path('client_project_details7',views.client_project_details7),
    path('client_project_details8',views.client_project_details8),
    path('client_project_details9',views.client_project_details9),
    path('client_project_details10',views.client_project_details10),
    
    
]
