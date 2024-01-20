from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def registeration(request):
    ufo = UserForm()
    pfo = ProfileForm()
    d = {'ufo':ufo,'pfo':pfo}
    
    if request.method == 'POST' and request.FILES:
        ufd = UserForm(request.POST)
        pfd = ProfileForm(request.POST,request.FILES)

        if ufd.is_valid() and pfd.is_valid():
            MUFDO = ufd.save(commit=False)
            pw = ufd.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO = pfo.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            return HttpResponse('registeration is completed')
        else:
            return HttpResponse('invalid data')

    return render(request,'registeration.html',d)
