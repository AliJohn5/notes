
from django.urls import path
from .views import NoteDetailView, NoteListCreateView, RegisterView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
