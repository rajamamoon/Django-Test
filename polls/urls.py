from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.home_view, name='index'),
    path('<student_name>', views.name_view, name='student'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]