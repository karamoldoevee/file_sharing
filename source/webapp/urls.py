from django.urls import path
from webapp.views import FileListView, FileDetailView, FileCreateView, FileUpdateView, FileDeleteView, AddToPrivate, \
    DeleteFromPrivate

urlpatterns = [
    path('', FileListView.as_view(), name='index'),
    path('file/create/', FileCreateView.as_view(), name='file_create'),
    path('file/detail/<int:pk>/', FileDetailView.as_view(), name='file_detail'),
    path('file/update/<int:pk>/', FileUpdateView.as_view(), name='file_update'),
    path('file/delete/<int:pk>/', FileDeleteView.as_view(), name='file_delete'),
    path('product/add-to-private/', AddToPrivate.as_view(), name='add_to_private'),
    path('product/delete-from-private/', DeleteFromPrivate.as_view(), name='delete_from_private')
]

app_name = 'webapp'
