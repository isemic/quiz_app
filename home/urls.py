from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('', views.home , name = 'home'),
   path('quiz/', views.quiz, name= 'quiz'),
   path('api/get-quiz/', views.get_quiz, name='get_quiz'),
   path('quiz/submit/', views.submit_quiz, name='submit_quiz'),
   path('quiz/result/', views.result_view, name='quiz_result'),
   
]