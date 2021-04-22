from django.urls import path
from . import views

app_name = 'manager'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('add_user', views.AddUserView.as_view(), name='add_user'),
    path('add_transaction', views.AddTranscationView.as_view(), name='add_transaction')
]