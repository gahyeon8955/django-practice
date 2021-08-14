from django.urls import path
import mainapp.views

urlpatterns = [
    path('<int:blog_id>/', mainapp.views.detail, name='detail'),
    path('new/', mainapp.views.new, name='new'),
    path('create', mainapp.views.create, name='create'),
]