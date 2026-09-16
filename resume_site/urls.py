from django.urls import path

from resume.views import resume

urlpatterns = [path("", resume, name="resume")]