from django.shortcuts import render
from .models import Entry

def index(request):

    entries = Entry.objects.all()

    return render(request, 'myapp/index.html', { 'entries': entries })