from django.urls import path, include

from callendar.views import ListCallendar

urlpatterns = [
    path('',  ListCallendar.as_view())
]
