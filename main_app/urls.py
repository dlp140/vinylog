from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records, name='records'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/add/', views.RecordCreate.as_view(), name='records_add'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('collections/', views.collections, name='collections'),
    path('accounts/signup', views.signup, name='signup'),
    path('records/<int:record_id>/add_photo', views.add_photo, name='add_photo')
]
