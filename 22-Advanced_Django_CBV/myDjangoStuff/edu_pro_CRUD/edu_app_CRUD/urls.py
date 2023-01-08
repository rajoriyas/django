from django.urls import path
from edu_app_CRUD import views

app_name = 'edu_app_CRUD'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='school_list'),
    path('<int:pk>/', views.SchoolDetailView.as_view(), name='school_detail'),
    #path('create/', views.SchoolCreateView.as_view(), name='school_create'),
    path('create/', views.create, name='school_create'),
    path('update/<int:pk>/', views.SchoolUpdateView.as_view(), name='school_update'),
    path('delete/<int:pk>/', views.SchoolDeleteView.as_view(), name='school_delete'),
    path('student/modify/<int:pk>/', views.StudentDeleteView.as_view(), name='student_delete'),
    path('student/update/<int:pk>/', views.StudentUpdateView.as_view(), name='student_update'),
]
