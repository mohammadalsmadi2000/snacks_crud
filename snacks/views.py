from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
from .models import Snack

class HomePageView(TemplateView):
    template_name='home.html'


class SnackListView(ListView):
    template_name='snack_list.html'
    model=Snack
    context_object_name="snacks"

class SnackDetailView(DetailView):
    template_name="snack_detail.html"
    model=Snack 


class SnackCreateView(CreateView):
    template_name="snack_create.html"
    model=Snack
    fields="__all__"
# class SnackUpdateView(UpdateView):
#     template_name='thing_update.html'
#     model=Snack
#     fields="__all__"
#     success_url=reverse_lazy('')


# class SnackDeleteView(DeleteView):
#     template_name="D"
#     model=Snack
#     success_url=reverse_lazy('')