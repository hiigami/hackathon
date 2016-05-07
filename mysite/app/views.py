from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Contratar(View):
    template_name = 'app/contratar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)