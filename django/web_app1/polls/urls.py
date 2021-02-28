from django.urls import path
from polls import views

app_name = 'polls' # polls 앱의 namespace명


urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
]