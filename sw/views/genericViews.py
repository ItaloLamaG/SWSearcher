from django.views.generic.base import View
from django.shortcuts import render
from sw.models.film import Film
from sw.models.people import People
from sw.models.planet import Planet
from sw.models.species import Species
from sw.models.transport import Starship, Vehicle


MODELS = {
    "Planet": Planet,
    "People": People,
    "Starship": Starship,
    "Vehicle": Vehicle,
    "Species": Species,
    "Film": Film,
}


class generalGet(View):
    def get(self, request, *args, **kwargs):
        if len(kwargs) == 4:
            id_ = kwargs["id"]
            return render(
                request,
                kwargs["template"],
                context={
                    kwargs["context_name"]: MODELS[kwargs["model"]].objects.get(id=id_)
                },
            )
        else:
            return render(
                request,
                kwargs["template"],
                context={kwargs["context_name"]: MODELS[kwargs["model"]].objects.all()},
            )
