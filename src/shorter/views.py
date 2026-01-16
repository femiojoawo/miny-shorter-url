from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from shorter.form import ShorterUrlForm
from shorter.models import ShortUrl
from shorter.shorter_algo import shorter_algo
from django.urls import reverse
# Create your views here.


def shorturl(request):
    context = {}
    if request.method == 'POST':
        form = ShorterUrlForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            try:
                short = ShortUrl.objects.get(true_url=form.cleaned_data["url"])
                context['info'] = "l'url existe deja"
                context["reverse_url"] = f"{reverse('index-short')}/{short.short_suffix}"
            except ShortUrl.DoesNotExist:
                created = ShortUrl.objects.create(true_url=form.cleaned_data["url"], short_suffix=shorter_algo(form.cleaned_data["url"]))
                created.save()
                context["reverse_url"] = f"{reverse('index-short')}/{ShortUrl.objects.get(true_url=form.cleaned_data["url"]).short_suffix}"
            
    else:
        form = ShorterUrlForm()
    context['form'] = form
    return render(request,'shorter/index.html',context)

def reverse_url(request,url):
    short = get_object_or_404(ShortUrl, short_suffix = url)
    short.num_use += 1
    short.save()
    return  HttpResponseRedirect(short.true_url)