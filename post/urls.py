from django.urls import path
from .views import PostDetailView, HomeView, Archive

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('archive/', Archive.as_view(), name='archive'),
    path('archive/series/<slug:slug>/', Archive.as_view(), name='series'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post-detail'),
]
