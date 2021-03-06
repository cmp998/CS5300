from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('library/', views.library, name="library"),
    path('library/<int:book_id>', views.libraryBook, name="library"),
    path('authors/', views.author, name="authors"),
    path('authorsbooks/<int:authorID>', views.authorBooks, name="authors"),
    path('dashboard/', views.dashboard, name='dashboard')
]