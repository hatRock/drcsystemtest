from django.shortcuts import render
from django.views import View

from apps.users.forms import ProfileForm


class Register(View):
    form = ProfileForm
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        return render(request, self.template_name)