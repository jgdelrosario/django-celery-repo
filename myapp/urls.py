from django.urls import path
from myapp.views import AddView

app_name = 'myapp'

urlpatterns = [
    path('add/', AddView.as_view(), name='add'),
]