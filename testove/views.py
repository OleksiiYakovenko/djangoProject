from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CreateNewList
from .models import GeneratedCSV, Item
from django.template import loader
from django.urls import reverse
# Create your views here.


def index(response, id):
    ls = GeneratedCSV.objects.get(id=id)
    if response.method == 'POST':
        if response.POST.get('newItem') == 'clicked':
            colum_name = response.POST.get('colum_name')
            type = response.POST.get('type')
            order = response.POST.get('order')
            if len(colum_name) > 0:
                ls.item_set.create(name=colum_name, type=type, order=order)
        elif response.POST.get('save'):
            for item in ls.item_set.all():
                item.save()
    return render(response, 'testove/list.html', {'ls': ls})


def home(response):
    return render(response, 'registration/login.html', {})


def create(response):
    if response.method == 'POST':
        form = CreateNewList(response.POST)
        if form.is_valid():
            n = form.cleaned_data['name']
            t = GeneratedCSV(name=n)
            t.save()
            response.user.generatedCSV.add(t)
        return HttpResponseRedirect('/%i' %t.id)
    else:
        form = CreateNewList()
    return render(response, 'testove/create.html', {'form': form})


def view(response):
    return render(response, 'testove/view.html', {})


def delete(response, id):
    number = GeneratedCSV.objects.get.id
    print(number)
    item = Item.objects.get(id=id)
    item.delete()
    return render(response, 'testove/list.html', {'ls': ls})
