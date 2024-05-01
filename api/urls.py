from django.urls import path
from . import views

urlpatterns = [
    path('quiz-list/', views.QuizlistView.as_view()),
    path('quiz-list-create/', views.QuizlistCreateView.as_view()),

    # <<<<<<<<<<<<<< Quisitions list, listcreate >>>>>>>>>>>>>>>>>>>>

    path('quistion-list/', views.QuestionListView.as_view()),
    path('quistion-list-create/', views.QuestionCreateView.as_view()),

    # <<<<<<<<<<<< option list , listcreate >>>>>>>>>>>

    path('option-list/', views.OptionListView.as_view()),
    path('option-list-create/', views.OptionCreateView.as_view()),


]