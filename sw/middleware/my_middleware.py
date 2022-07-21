from django.conf import settings


class visits_middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)
        request_path = request.get_full_path()
        if (
            not request.path.startswith(settings.STATIC_URL)
            and not request.path.startswith("/admin")
            and not request.path.startswith("/login")
            and not request.path.startswith("/logout")
        ):
            try:
                saved = request.session["last_pages"]
                saved.append(request_path)
                saved = list(dict.fromkeys(saved))
                request.session["last_pages"] = saved[-10:]
            except Exception:
                request.session["last_pages"] = [request_path]
        # Code to be executed for each request/response after
        # the view is called.
        return response
