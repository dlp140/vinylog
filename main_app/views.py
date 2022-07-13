import uuid
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from .models import Record, Collection, Photo
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.detail import DetailView
import uuid
import boto3

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'vinylog'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def records(request):
    records = Record.objects.all()
    photos = Photo.objects.all()
    return render(request, 'records/index.html', { 'records': records, 'photos': photos })

def my_records(request):
  records = Record.objects.filter(user=request.user)
  return render(request, 'records/myrecords.html', { 'records': records })

# Work version without collection integration
def records_detail(request, record_id):
    record = Record.objects.get(id=record_id)
    collection = Collection.objects.filter()
    return render(request, 'records/detail.html', { 'record': record, 'collection': collection })

# Collection integration
# def records_detail(request, record_id):
#     record = Record.objects.get(id=record_id)
#     collections_record_not_in = Collection.objects.exclude(id__in = record.collections.all().values_list('id'))
#     return render(request, 'records/detail.html', { 'record': record, 'collections': collections_record_not_in })

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


def assoc_record(request, collection_id, record_id):
    Collection.objects.get(id=collection_id).records.add(record_id)
    return redirect('detail', record_id=record_id)

# def collections_detail(request, collection_id):
#     collection = Collection.objects.get(collection_id)
#     return render(request, 'collections/detail.html', { 'collection': collection})

# class CollectionList (ListView):
#     model = Collection
#     template_name = 'collections/index.html'

class CollectionDetail (DetailView):
    model = Collection
    template_name = 'collections/detail.html'


@login_required
def add_photo(request, record_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, record_id=record_id)
            photo.save()
        except Exception as error:
            print('An error occurred uploading file to S3', error)
            return redirect('detail', record_id=record_id)
    return redirect('detail', record_id=record_id)

def signup(request):
    error_messages = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        try:
            user = form.save()
            login(request, user)
            return redirect('records')
        except:
            error_messages = form.errors
    form = UserCreationForm()
    context = {'form': form, 'error_messages': error_messages}
    return render(request, 'registration/signup.html', context)