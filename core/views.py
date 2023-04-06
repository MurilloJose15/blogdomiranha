from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from core.models import Post

#class IndexView(TemplateView):
#    template_name = "index.html"

class ListarPostsListView(ListView):
    context_object_name = 'posts'
    template_name = 'index.html'
    queryset = Post.publicados.all()
    paginate_by = 3