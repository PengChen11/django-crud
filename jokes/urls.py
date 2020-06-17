from django.urls import path
from .views import *

urlpatterns = [
    path('', JokesListView.as_view(), name='list'),
    path('content/<int:pk>/', JokesDetailsView.as_view(), name='details'),
    path('content/new/', JokesCreateView.as_view(), name='new'),
    path('content/<int:pk>/edit/', JokesUpdateView.as_view(), name='update'),
    path('content/<int:pk>/delete/', JokesDeleteView.as_view(), name='delete'),

]
