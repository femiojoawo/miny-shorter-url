from django.shortcuts import render
from shorter.form import ShorterUrlForm
from shorter.models import ShortUrl
from shorter.shorter_algo import shorter_algo
# Create your views here.


def shorturl(request):
    if request.method == 'POST':
        form = ShorterUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            short = ShortUrl.objects.create(true_url=form.cleaned_data["url"], short_url= shorter_algo(form.cleaned_data["url"]))
            short.save()
    else:
        form = ShorterUrlForm()
    context = {"form":form}
    return render(request,'shorter/index.html',context)