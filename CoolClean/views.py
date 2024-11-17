from CoolClean.mixin import AuthorizationRequiredMixin
from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class NewPosition(AuthorizationRequiredMixin, View):
    def get(self, request):
        return render(request, "new_position.html")
