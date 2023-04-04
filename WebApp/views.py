from django.shortcuts import render

# Create your views here.
def Home_View(request):
    return render(request,'MyApp/home.html')
def about_View(request):
    return  render(request,'MyApp/about.html')
def News_View(request):
    return  render(request,'MyApp/news.html')
def Clients_View(request):
    return  render(request,'MyApp/clients.html')
def Employee_View(request):
    return  render(request,'MyApp/employee.html')
def Works_View(request):
    return  render(request,'MyApp/works.html')
def Login_View(request):
    return render(request,'MyApp/login.html')



