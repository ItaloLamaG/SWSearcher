from django.views.generic.base import View
from django.shortcuts import render
from django.db.models import Q
from sw.models.film import Film
from sw.models.historic import Historic


class SearchTemplateView(View):
    def get(self, request):
        query = self.request.GET.get("q")
        if query:
            result = Film.objects.filter(
                Q(title__icontains=query)
                | Q(opening_crawl__icontains=query)
                | Q(director__icontains=query)
                | Q(producer__icontains=query)
                | Q(release_date__icontains=query)
                | Q(characters__name__icontains=query)
                | Q(planets__name__icontains=query)
            ).distinct()
            for film in result:
                Historic.objects.create(film=film)
        else:
            result = None
        return render(request, "films/search_list.html", context={"films": result})
