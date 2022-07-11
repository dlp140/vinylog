from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Record, Collection
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records(request):
    records = Record.objects.all()
    return render(request, 'records/index.html', { 'records': records })

def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    return render(request, 'records/detail.html', { 'record': record })

class RecordCreate(LoginRequiredMixin, CreateView):
    model = Record
    fields = ['artist', 'title', 'release_date', 'genre', 'description', 'notes', 'condition' ]
    succes_url = '/records/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class RecordUpdate(LoginRequiredMixin, UpdateView):
    model = Record
    fields = ['description']

class RecordDelete(LoginRequiredMixin, DeleteView):
    model = Record
    success_url = '/records/'

def collections(request):
    collections = Collection.objects.all()
    return render(request, 'collections/index.html', { 'collections': collections })

def signup(request):
    error_messages = ''
    # Check if the request method is POST
    if request.method == 'POST':
        # This is how to create a 'user' form object that includes the data from the browser
        form = UserCreationForm(request.POST)
        try:
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('records')
        except:
            error_messages = form.errors
    #A body POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_messages': error_messages}
    return render(request, 'registration/signup.html', context)