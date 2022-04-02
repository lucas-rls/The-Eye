from django.urls import path
from .views import home, form


urlpatterns = [path("", home), path("form/", form)]
