from django.urls import path
from sw.views.index import IndexTemplateView
from sw.views.searchViews import SearchTemplateView
from sw.views.genericViews import generalGet


urlpatterns = [
    path("", IndexTemplateView.as_view(), name="index"),
    path("search/", SearchTemplateView.as_view(), name="search_list"),
    path(
        "films",
        generalGet.as_view(),
        {"model": "Film", "context_name": "film", "template": "films/films.html"},
        name="films",
    ),
    path(
        "films/<int:id>/",
        generalGet.as_view(),
        {
            "model": "Film",
            "context_name": "film",
            "template": "films/filmsDetails.html",
        },
        name="film",
    ),
    path(
        "characters",
        generalGet.as_view(),
        {
            "model": "People",
            "context_name": "characters",
            "template": "characters/characters.html",
        },
        name="characters",
    ),
    path(
        "characters/<int:id>/",
        generalGet.as_view(),
        {
            "model": "People",
            "context_name": "charac",
            "template": "characters/charactersDetails.html",
        },
        name="character",
    ),
    path(
        "planets",
        generalGet.as_view(),
        {
            "model": "Planet",
            "context_name": "planets",
            "template": "planets/planets.html",
        },
        name="planets",
    ),
    path(
        "planets/<int:id>/",
        generalGet.as_view(),
        {
            "model": "Planet",
            "context_name": "planet",
            "template": "planets/planetsDetails.html",
        },
        name="planet",
    ),
    path(
        "species",
        generalGet.as_view(),
        {
            "model": "Species",
            "context_name": "species",
            "template": "species/species.html",
        },
        name="species",
    ),
    path(
        "species/<int:id>/",
        generalGet.as_view(),
        {
            "model": "Species",
            "context_name": "species",
            "template": "species/speciesDetails.html",
        },
        name="specie",
    ),
    path(
        "starships",
        generalGet.as_view(),
        {
            "model": "Starship",
            "context_name": "starships",
            "template": "starships/starships.html",
        },
        name="starships",
    ),
    path(
        "starships/<int:id>/",
        generalGet.as_view(),
        {
            "model": "Starship",
            "context_name": "starship",
            "template": "starships/starshipsDetails.html",
        },
        name="starship",
    ),
    path(
        "vehicles",
        generalGet.as_view(),
        {
            "model": "Vehicle",
            "context_name": "vehicles",
            "template": "vehicles/vehicles.html",
        },
        name="vehicles",
    ),
    path(
        "vehicles/<int:id>/",
        generalGet.as_view(),
        {
            "model": "Vehicle",
            "context_name": "vehicle",
            "template": "vehicles/vehiclesDetails.html",
        },
        name="vehicle",
    ),
]
