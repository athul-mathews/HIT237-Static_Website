from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'as2_app/home.html')
def projectlist(request):
    return render(request, 'as2_app/projectlist.html')
 