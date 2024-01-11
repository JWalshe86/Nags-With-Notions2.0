from django.urls import path as url

from django_summernote.views import (
    SummernoteEditor, SummernoteUploadAttachment
)

urlpatterns = [
    url('summernote/', SummernoteEditor.as_view(),
        name='django_summernote-editor'),
    url('summernote/', SummernoteUploadAttachment.as_view(),
        name='django_summernote-upload_attachment'),
]