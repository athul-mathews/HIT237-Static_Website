from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'as2_app/home.html')
def projectlist(request):
    return render(request, 'as2_app/projectlist.html')

def about(request):
    return render(request, 'as2_app/about.html')

def project_details(request):
    pass
 