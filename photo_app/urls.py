from django.urls import path
from . import views

app_name = 'photos'

urlpatterns = [
    path('', views.PhotosList.as_view(), name='photos_list'),
    path('<int:pk>', views.PhotoDetail.as_view(), name='photo_detail')
]