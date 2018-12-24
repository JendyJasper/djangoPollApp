from django.urls import path
from . import views

urlpatterns = [
	
	# 127.0.0.1/polls
	path('', views.index, name="index"),

	# 127.0.0.1/polls/1
	path('<int:question_id>/', views.detail, name="detail"),

	# 127.0.0.1/polls/1/results
	path('<int:question_id>/results', views.results, name="results"),

	# 127.0.0.1/polls/1/vote
	path('<int:question_id>/vote', views.vote, name="vote"),

]