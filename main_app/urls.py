from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records_index, name='index'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/add/', views.RecordCreate.as_view(), name='records_add'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
]
