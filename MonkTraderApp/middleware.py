from django.http import Http404
from django.urls import reverse

def hide_django_admin_middleware(get_response):
    def middleware(request):
        # Check if the request path starts with the admin index path
        if request.path.startswith(reverse('admin:index')):
            # If the user is not staff, raise a 404 error
            if not request.user.is_staff:
                raise Http404()
        return get_response(request)

    return middleware