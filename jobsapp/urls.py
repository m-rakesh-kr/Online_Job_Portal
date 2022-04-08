from django.urls import path, include

from .views import *

app_name = "jobs"

urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('all-company', CompanyListView.as_view(), name='employer-all-company'),
]

