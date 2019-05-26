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
    return render(request, 'facts.html')

def test(request):
    return render(request, 'test.html')