from django.urls import path
from . import views
from .views import CreateFolderView

urlpatterns =[
    path('', views.home, name='home'),
    path('<int:pk>/', views.files, name='files'),
    path('<int:pk>/upload_file/', views.upload_files, name='upload_file'),
    path('create_folder/', CreateFolderView.as_view(), name="create_folder"),

]