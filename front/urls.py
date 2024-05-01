from . import views
from django.urls import path


urlpatterns = [
    # ------- Error --------
    path('', views.eror, ),
    # ------- Quiz detail --------
    path('<str:code>/', views.quiz_detail)
]