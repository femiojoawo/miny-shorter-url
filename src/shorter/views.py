from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from shorter.form import ShorterUrlForm
from shorter.models import ShortUrl
from shorter.shorter_algo import shorter_algo
from django.urls import reverse
from django.utils.text import slugify
# Create your views here.

def shorturl(request):
    context = {}
    if request.method == 'POST':
        form = ShorterUrlForm(request.POST)
        if form.is_valid():
            try:
                short = ShortUrl.objects.get(true_url=form.cleaned_data["url"])
                context['url_exist'] = True
                context["reverse_url"] = f"{reverse('index-short')}/{short.slug}"
                context['url_exist'] = True
                context["reverse_url"] = f"{reverse('index-short')}/{short.slug}"
            except ShortUrl.DoesNotExist:
                created = ShortUrl.objects.create(true_url=form.cleaned_data["url"], slug=slugify(form.cleaned_data['slug']))
                created.save()
                context['url_exist'] = False
                context["reverse_url"] = f"{reverse('index-short')}/{ShortUrl.objects.get(true_url=form.cleaned_data["url"]).slug}"
                context['url_exist'] = False
                context["reverse_url"] = f"{reverse('index-short')}/{ShortUrl.objects.get(true_url=form.cleaned_data["url"]).slug}"
            
    else:
        form = ShorterUrlForm()
    context['form'] = form
    return render(request,'shorter/index.html',context)

def reverse_url(request,url):
    short = get_object_or_404(ShortUrl, slug = url)
    short = get_object_or_404(ShortUrl, slug = url)
    short.num_use += 1
    short.save()
    return  HttpResponseRedirect(short.true_url)