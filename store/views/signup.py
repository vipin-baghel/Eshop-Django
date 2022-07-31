from django.views import View
from django.shortcuts import render, redirect
from store.models import Customer

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        post_data = request.POST
        customer = Customer.from_post(post_data)  # convert post data to customer object
        values = vars(customer)  # convert customer object to dict
        error_message = customer.validate()  # validate customer
        if not error_message:
            customer.register()  # save customer to DB if validations succeed
            return redirect('homepage')  # redirect to home page
        else:
            return render(request, 'signup.html',
                          {'error': error_message, 'values': values})  # show errors & pass customer values to front end

