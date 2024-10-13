from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')
def basketball(request):
    return render(request, 'pages/basketball.html')
def about(request):
    return render(request, 'pages/about.html')