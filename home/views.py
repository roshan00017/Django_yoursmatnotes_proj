from re import template
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


# function based

""" def home (request):
    return render(request,'home/welcome.html',{'today':datetime.today()})
 """

#class based

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    
    extra_context = {'today':datetime.today()}

#function based
""" @login_required
def authorize(request):
    return render(request,'home/authorize.html',{}) """

#class based

class AuthorizeView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorize.html'
    login_url = '/admin'
    


