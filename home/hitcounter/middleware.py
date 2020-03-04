from .tasks import save_hit

class HitCounterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        if request.user.is_authenticated and 'admin' not in view_func.__module__:
            print("save hit")
            save_hit(request.user.pk, "{}:{}".format(view_func.__module__, view_func.__name__))
        return None
