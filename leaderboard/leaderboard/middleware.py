from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import render
from social.exceptions import AuthCanceled,AuthForbidden
from django.http import HttpResponse, HttpResponseBadRequest

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
    def process_exception(self, request, exception):
        if type(exception) == AuthCanceled:
            return render(request, "signup.html", {})
        elif type(exception) == AuthForbidden:
            return render(request, "signup.html", {"error_message": "Login using your Colorado.edu email ID"})
        else:
            return HttpResponse("Error! Report to the administrator")