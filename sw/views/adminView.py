from django.views.generic.base import View
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.shortcuts import redirect

from sw.models.film import Film
from sw.models.people import People
from sw.models.planet import Planet
from sw.models.species import Species
from sw.models.transport import Starship, Vehicle
from sw.utils.manage_data import loader

MODELS = {
    "Planets": Planet.objects.count(),
    "People": People.objects.count(),
    "Starships": Starship.objects.count(),
    "Vehicles": Vehicle.objects.count(),
    "Species": Species.objects.count(),
    "Films": Film.objects.count(),
}


class adminView(LoginRequiredMixin, View):
    login_url = "/login/"

    def get(self, request):
        return render(request, "admin.html", context={"models": MODELS})


class logoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login/")


def loadData(request):
    if request.method == "POST":
        loader.exec()
    return redirect("admin")
