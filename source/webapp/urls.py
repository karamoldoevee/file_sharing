from django.urls import path
from webapp.views import FileListView, FileCreateView, FileUpdateView, FileDeleteView

urlpatterns = [
    path('', FileListView.as_view(), name='index'),
    path('file/create/', FileCreateView.as_view(), name='file_create'),
    path('file/update/<int:pk>/', FileUpdateView.as_view(), name='file_update'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
]

app_name = 'webapp'
