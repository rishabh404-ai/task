
from django.urls import path
from app.views import RegisterView, RecordEntryView, home

urlpatterns = [
    path('',home),
    path('register/',RegisterView.as_view()),
    path('entry/',RecordEntryView.as_view())
]
