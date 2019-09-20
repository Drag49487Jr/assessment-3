from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .models import Wish




def home(request):
    wishs=Wish.objects.all()
    wish_counter=wishs.count()
    return render(request, 'index.html', {
        'wishs':wishs,
        'wish_counter':wish_counter,
        })

class WishCreate(CreateView):
    model = Wish
    fields = '__all__'
    success_url='/'

class WishDelete(DeleteView):
    model = Wish
    success_url='/'