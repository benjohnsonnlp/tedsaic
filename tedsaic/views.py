from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from tedsaic.models import Image


def index(request):
    context = {
        'images': Image.objects.all(),
    }
    return render(request, "tedsaic/index.html", context=context)

def add_image(request):
    url = request.POST['url']
    # save the url
    image = Image(url=url)
    image.save()
    # send them back to the normal page
    return HttpResponseRedirect(reverse('index'))