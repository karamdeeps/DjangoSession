from django.urls import path

from .views import Data, Session

urlpatterns = [
    path('data/', Data.as_view()),
    path('session/', Session.as_view())
]