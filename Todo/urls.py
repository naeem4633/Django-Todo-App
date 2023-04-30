from django.urls import path
from . import views
from .views import TodoCreateView, TodoDeleteView, TodoIndexView, TodoUpdateView

app_name = 'Todo'

urlpatterns = [
    path('', TodoIndexView.as_view(), name='index'),
    path('delete/<int:pk>/', TodoDeleteView.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdateView.as_view(), name='update'),
    path('create/', TodoCreateView.as_view(),name='create'),
]