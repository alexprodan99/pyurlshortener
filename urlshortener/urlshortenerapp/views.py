from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import ShortenerItem
from .forms import ShortenerForm


def home_view(request):
    context = {}
    context['form'] = ShortenerForm()

    if request.method == 'GET':
        return render(request, 'home.html', context)
    elif request.method == 'POST':
        form = ShortenerForm(request.POST)
        if form.is_valid():
            shortener_item = form.save()
            new_url = request.build_absolute_uri('/') + shortener_item.short_url
            long_url = shortener_item.long_url
            context['new_url'] = new_url
            context['long_url'] = long_url
            return render(request, 'home.html', context)
    context['errors'] = form.errors
    return render(request, 'home.html', context)


def redirect_url_view(request, short_url):
    try:
        shortener = ShortenerItem.objects.get(short_url=short_url)
        return HttpResponseRedirect(shortener.long_url)
    except:
        raise Http404('Broken link')
