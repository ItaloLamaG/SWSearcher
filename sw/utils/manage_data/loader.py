import requests
from sw.models.people import People
from sw.models.planet import Planet
from sw.models.film import Film
from sw.models.species import Species
from sw.models.transport import Vehicle, Starship


MODELS = {
    "planets": Planet,
    "people": People,
    "starships": Starship,
    "vehicles": Vehicle,
    "species": Species,
    "films": Film,
}

RELATED = {
    "homeworld": Planet,
    "pilots": People,
    "people": People,
    "characters": People,
    "planets": Planet,
    "starships": Starship,
    "vehicles": Vehicle,
    "species": Species,
}

IGNORE = {
    Planet: ["created", "edited", "residents", "films"],
    Starship: ["created", "edited", "films"],
    Vehicle: ["created", "edited", "films"],
    People: ["created", "edited", "films", "species", "vehicles", "starships"],
    Species: ["created", "edited", "films"],
    Film: ["created", "edited"],
}

BASEURL = "https://swapi.co/api/"


def _query(model: str) -> str:
    if model.startswith("http"):
        return model
    else:
        return BASEURL + model


def _get_id(url: str) -> str:
    return url.rsplit("/", 2)[1]


def _save_page(model, data):
    ignored_keys = IGNORE[model]
    for element in data:
        instance = model()
        many_to_many = {}
        for key, value in iter(element.items()):
            # get id from url
            if key == "url":
                key = "id"
                value = _get_id(value)
            if key in RELATED and key not in ignored_keys:
                # primary key relationship
                if not isinstance(value, list) and value is not None:
                    related = RELATED[key].objects.get(pk=_get_id(value))
                    setattr(instance, key, related)
                # many to many relationship
                elif value is not None:
                    many_to_many[key] = value
            # normal values
            elif key not in ignored_keys:
                setattr(instance, key, value)
        # save object
        instance.save(force_insert=True)
        # make many to many relationships
        for mkey, mvalues in iter(many_to_many.items()):
            for url in mvalues:
                related = RELATED[mkey].objects.get(pk=_get_id(url))
                getattr(instance, mkey).add(related)


# Drop all models
def _drop():
    for model in MODELS.values():
        model.objects.all().delete()


def _load():
    for name, model in iter(MODELS.items()):
        next = True
        while next:
            try:
                res = requests.get(_query(name)).json()
            except Exception:
                pass
            _save_page(model, res["results"])
            if bool(res["next"]):
                name = res["next"]
            else:
                next = False


def exec():
    _drop()
    _load()
