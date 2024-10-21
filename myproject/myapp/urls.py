from django.urls import path
import myapp.views as views

urlpatterns = [
    path("add_note/", views.add_note, name="add_note"),
    path('', views.NoteListView.as_view(), name='note_list'),
    path('note_detail/<int:pk>/', views.NoteDetailView.as_view(), name='note_detail'),
]