from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin

def db_home(request):
    service = Artikles.objects.all()
    return render(request,'datebase/db_home.html', {'service': service})

class Detail_home(DetailView):
    model = Artikles
    template_name = 'datebase/detail_home'
    context_object_name = 'kay'

def index(request):
    query_results = Artikles.objects.all()
    location_list = LocationChoiceField()

    context = {
        'query_results': query_results,
        'location_list': location_list,

    }
    return render(request,'datebase/add_coment.html', context)

def coment(request):
    coment = Coment.objects.all()
    return render(request, 'datebase/coment.html', {'coment': coment})

def add_coment(request):
    error = ''
    if request.method == "POST":
        form = Comentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('coment')
        else:
            error = "форма была не верной"


    form = Comentform

    date ={
        'form': form,
        'eror': error,

    }
    return render(request, 'datebase/add_coment.html', date)



