from django.urls import path, include
from education_app import views

app_name = 'education_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school_list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
]
