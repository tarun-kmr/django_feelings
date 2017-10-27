from braces.views import SelectRelatedMixin
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.views import generic

from . import forms


class DashboardView(LoginRequiredMixin,
                    generic.DetailView,
                    SelectRelatedMixin):
    model = User
    select_related = ('thoughts',)
    template_name = "users/dashboard.html"

    def get_object(self, queryset=None):
        return self.request.user


def logout_view(request):
    logout(request)


class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "users/signup.html"
    success_url = reverse_lazy("home")


class CompanyCreateView(LoginRequiredMixin,
                        generic.CreateView):
    form_class = forms.CompanyForm
    template_name = 'users/company_form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response
