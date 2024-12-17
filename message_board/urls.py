from django.urls import path
from .views import ListPageView,DetailPageView

urlpatterns = [
    path("",ListPageView.as_view(),name="List-View"),
    path("posts/<int:pk>/",DetailPageView.as_view(),name="post-detail")
]



