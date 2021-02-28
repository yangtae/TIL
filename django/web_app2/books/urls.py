from django.urls import path
from . import views
import books

app_name = 'books'

urlpatterns = [
    # /books/
    path('',views.BooksModelView.as_view(), name = 'index'),
    
]