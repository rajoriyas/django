from django.urls import path
from first_app_with_template_inheritance import views

app_name = 'first_app_with_template_inheritance'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),
]
