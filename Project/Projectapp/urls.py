from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('', views.hi, name="Introduction"),
    path('Statistics', views.Statistics, name="Statistics"),
    path('Summary', views.Summary, name="Summary"),
]
urlpatterns += staticfiles_urlpatterns()