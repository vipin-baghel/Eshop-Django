from django.http import HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from store.models import Customer


class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.by_email(email)
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['cid'] = customer.id
                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Password is incorrect !'
        else:
            error_message = 'This email is not registered ! '

        return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('loginpage')