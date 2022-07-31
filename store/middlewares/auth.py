from django.shortcuts import redirect


def auth_middleware(get_response):

    def middleware(request):
        print("middleware start")
        print(request.META['PATH_INFO'])
        from_url = request.META['PATH_INFO']
        if not request.session.get('cid'):
            print('customer is not logged in, redirecting to login page')
            return redirect(f'login?return_url={from_url}')
        response = get_response(request)
        print("middleware end")
        return response
    return middleware
