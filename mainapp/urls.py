from django.urls import path
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('<int:blog_id>/', views.detail, name='detail'),
    path('new/', views.new, name='create'),
    path('<int:blog_id>/delete/', views.delete, name='delete'),
    path('<int:blog_id>/update/', views.update, name='update'),
]