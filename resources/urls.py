from django.urls import path
from .views import BookListCreateView, BookRetrieveUpdateDeleteView

urlpatterns = [
    path('resources/', BookListCreateView.as_view(), name='book-list-create'),
    path('resources/<int:pk>/', BookRetrieveUpdateDeleteView.as_view(), name='book-detail'),
]

