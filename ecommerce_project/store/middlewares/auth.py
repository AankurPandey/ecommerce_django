from django.shortcuts import redirect
# from .view import login

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        if not request.session.get('customerId'):
            return redirect('/login/')
        
        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware