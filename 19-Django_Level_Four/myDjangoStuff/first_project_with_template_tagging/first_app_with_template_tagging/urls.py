from django.urls import path, include
from . import views

app_name = 'first_app_with_template_tagging'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
