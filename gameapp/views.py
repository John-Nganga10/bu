from django.shortcuts import render

# Create your views here.
def collection(request):
    return render(request,'collection.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request, 'contact.html')