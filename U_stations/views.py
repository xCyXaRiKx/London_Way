from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from U_stations.models import fact, station, image


def index(request):

    context = {}
    context['facts'] = fact.objects.all()[:2]
    context['gallery'] = image.objects.all()[:8:-1]
    return render(request, 'index.html', context)

def facts(request):
    context = {}
    context['facts'] = fact.objects.all()
    return render(request, 'facts.html', context)

def gallery(request):
    context = {}
    context['images'] = image.objects.all()
    return render(request, 'gallery.html', context)

def test(request):
    return render(request, 'test.html')