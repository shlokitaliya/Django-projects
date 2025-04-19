from django.shortcuts import render
from .models import chaimenu,store
from django.shortcuts import get_object_or_404
from .forms import *

# Create your views here.
def learn(request):
    chai = chaimenu.objects.all()
    return render(request, 'learn/index.html',{"chai":chai})

def learn_detail(request,id):
    chai = get_object_or_404(chaimenu,pk = id)
    return render(request,'learn/learn_detail.html',{"chai":chai})
  
def chai_stores(request):
    stores = None
    if request.method =='POST':
        form = chaimenuform(request.POST)

        if form.is_valid():
            chai_menu = form.cleaned_data['chai_menu']
            stores = store.objects.filter(chai_menu=chai_menu )
    else:
        form = chaimenuform()

    return render(request, "learn/chai_stores.html",{"stores":stores,"form":form})