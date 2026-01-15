from django.shortcuts import render
from shorter.form import ShorterUrlForm
# Create your views here.
def shorturl(request):
    if request.method == 'POST':
        form = ShorterUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            
    else:
        form = ShorterUrlForm()
    context = {"form":form}
    return render(request,'shorter/index.html',context)