from django.shortcuts import render
from  django.views.generic import ListView,DetailView
from .models import Post
# Create your views here.


class ListPageView(ListView):

    template_name="ListView.html"
    model=Post
    
class DetailPageView(DetailView):

    template_name="DetailView.html"
    model=Post



    