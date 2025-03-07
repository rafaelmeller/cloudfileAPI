from django.urls import path
from .views import FileUploadView, FileListView, FileDetailView, FileDeleteView


urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file-upload'),
    path('', FileListView.as_view(), name='file-list'),
    path('<int:file_id>/', FileDetailView.as_view(), name='file-detail'),
    path('<int:file_id>/delete/', FileDeleteView.as_view(), name='file-delete'),
]
