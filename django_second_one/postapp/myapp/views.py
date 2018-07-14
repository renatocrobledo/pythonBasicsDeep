from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Entry
from .forms import EntryForm

def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', { 'entries': entries })

def details(request, pk):
    return render(request, 'myapp/details.html', { 'entry': Entry.objects.get(id=pk) })

def add(request):

    if request.method == 'POST':
        form = EntryForm(request.POST)

        if form.is_valid():

           ##implement insertion 
          title = form.cleaned_data['name']

          return HttpResponseRedirect('/')


    else:
      form = EntryForm()

    return render(request, 'myapp/form.html', { 'form': form })