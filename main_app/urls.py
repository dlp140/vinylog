from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('records/', views.records, name='records'),
    path('myrecords/', views.my_records, name='my_records'),
    path('records/<int:record_id>/', views.records_detail, name='detail'),
    path('records/add/', views.RecordCreate.as_view(), name='records_add'),
    path('records/<int:pk>/update/', views.RecordUpdate.as_view(), name='records_update'),
    path('records/<int:pk>/delete/', views.RecordDelete.as_view(), name='records_delete'),
    path('collections/', views.collections, name='collections'),
    # path('collections/', views.CollectionList.as_view(), name='collections'),
    path('collections/<int:pk>/', views.CollectionDetail.as_view(), name='collections_detail'),
    path('accounts/signup', views.signup, name='signup'),
    path('records/<int:record_id>/add_photo', views.add_photo, name='add_photo'),
    path('collections/<int:collection_id>/assoc_record/<int:record_id>/', views.assoc_record, name='assoc_record'),
]
