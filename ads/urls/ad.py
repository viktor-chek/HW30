from django.urls import path

from ads.views.ad import *

urlpatterns = [
    path('<int:pk>/upload_image/', AdUploadImage.as_view()),
]