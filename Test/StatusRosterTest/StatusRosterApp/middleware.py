# middleware.py
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser

class CurrentUserMiddleware(MiddlewareMixin):
    def process_request(self, request):
        request.current_user = request.user if request.user.is_authenticated else AnonymousUser()
