from django.views.generic.base import View
from django.shortcuts import render

from sw.models.film import Film
from django.db.models import Count


class IndexTemplateView(View):
    def get(self, request):
        result = Film.objects.annotate(visits=Count("historic")).order_by("-visits")[:5]
        return render(request, "index.html", context={"films": result})
