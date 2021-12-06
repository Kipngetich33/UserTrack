#other application imports
from django.urls import path,include

#application level import
from usertrack import views

urlpatterns = [
    path('', views.home, name='home')
]

