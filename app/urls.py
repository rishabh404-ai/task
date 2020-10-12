
from django.urls import path
from app.views import RegisterView, RecordEntryView

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('entry/',RecordEntryView.as_view())
]
