from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('scheduled_task/', views.scheduled_task, name='scheduled_task'),
    path('create_author/', views.create_author, name='create_author'),
    path('create_book/', views.create_book, name='create_book'),
    path('all_authors/', views.all_authors, name='all_authors'),
    path('send_email/', views.send_email, name='send_email'),


]