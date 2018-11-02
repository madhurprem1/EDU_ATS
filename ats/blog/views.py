from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.utils import timezone
from blog.models import Blog
# Create your views here.


class BlogView(TemplateView):
    template_name = 'blog.html'

    def get(self, request):
        posts = Blog.objects.all()
        return render(request, 'blog.html', {'posts': posts})

