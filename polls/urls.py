from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
	
	# 127.0.0.1/polls
	path('', views.IndexView.as_view(), name="index"),

	# 127.0.0.1/polls/1
	path('<int:pk>/', views.DetailView.as_view(), name="detail"),

	# 127.0.0.1/polls/1/results
	path('<int:pk>/results/', views.ResultsView.as_view(), name="results"),

	# 127.0.0.1/polls/1/vote
	path('<int:question_id>/vote/', views.vote, name="vote"),

]