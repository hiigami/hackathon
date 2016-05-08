from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from moneyed import *

globar_harcodeado = {
    "accountant" : {
        "price": Money(amount="120.00", currency='MXN'),
        "info": "",
        "photo": ""
    }
}

class Home(View):
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Contratar(View):
    template_name = 'app/contratar.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)

class Dashboard(View):
    template_name = 'app/dashboard.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

class DashboardUser(View):
    template_name = 'app/dashboard2.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)