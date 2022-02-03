from django.urls import path
from . import views

urlpatterns = [
    path('simpleapi', views.simpleapi, name='simple_api'),
    path('login', views.login, name='login_api'),
    path('borrowedbooks', views.borrowedbooks, name='borrowedbooks_api'),
]

#"token": "2930038aaccc5bb77a8bcdd5f31f1de269a72d7e"