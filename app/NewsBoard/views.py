from django.shortcuts import render
from django.views.generic import ListView
from django.views import View

from .models import Post


class Testing(View):
    template_name = 'NewsBoard/test_template.html'

    def get(self, request):
        context = dict()
        context['objects'] = Post.objects.all()

        return render(request, self.template_name, context)


