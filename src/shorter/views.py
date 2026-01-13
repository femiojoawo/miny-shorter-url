from django.shortcuts import render

# Create your views here.
def shorturl(request):
    return render(request,'shorter/index.html')