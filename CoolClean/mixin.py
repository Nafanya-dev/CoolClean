from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


AUTHORIZATION_MESSAGE = 'Нужны права администратора'


class AuthorizationRequiredMixin(LoginRequiredMixin):
    """
    Inherits from LoginRequiredMixin and checks
    whether the user is authenticated.
    If not, it displays an error message and redirects to the login page
    """
    authorization_message = AUTHORIZATION_MESSAGE

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.authorization_message)
            return redirect(reverse_lazy('home-page'))

        return super().dispatch(request, *args, **kwargs)
