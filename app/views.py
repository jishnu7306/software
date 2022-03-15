from django.shortcuts import render

# Create your views here.

#***********************  client  *******************************************************
def client_Dashboard(request):
    return render(request,'client\client_Dashboard.html')

def base_client(request):
     return render(request,'client\base_client.html')

def client_project_details(request):
    return render(request,'client\client_project_details.html')

def manager_attendance_show(request):
    return render(request,'manager\manager_attendance_show.html')

def client_company_card(request):
    return render(request,'client\client_company_card.html')

def client_company_details1(request):
    return render(request,'client\client_company_details1.html')

def client_company_details2(request):
    return render(request,'client\client_company_details2.html')

def client_company_details3(request):
    return render(request,'client\client_company_details3.html')


#***********************developer***********************************************
def index(request):
    return render(request,'index.html')



#******************  Manager ******************************************

def manager_Dashboard(request):
    return render(request,'manager\manager_Dashboard.html')


#****************** Project Manager ******************************************
    
