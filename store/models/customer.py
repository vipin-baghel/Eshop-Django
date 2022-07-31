from django.db import models
from django.contrib.auth.hashers import make_password, check_password


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def register(self):
        self.save()

    def by_email(email):
        try:
            return Customer.objects.get(email=email)
        except :
            return False

    def by_cid(cid):
        try:
            return Customer.objects.get(id=cid)
        except :
            return False

    def validate(self):
        # validations
        error_message = None
        if len(str(self.first_name)) < 4:
            error_message = 'First Name should be of minimum 4 characters'
        elif len(str(self.last_name)) < 4:
            error_message = 'Last Name should be of minimum 4 characters'
        elif len(str(self.phone)) != 10:
            error_message = 'Phone number should be of 10 digits'
        elif len(str(self.password)) < 6:
            error_message = 'Password should be atleast 6 char long'
        elif Customer.objects.filter(email=self.email):
            error_message = 'This Email is already registered'

        return error_message

    def from_post(post_data):
        firstname = post_data.get('FirstName')
        lastname = post_data.get('LastName')
        phone = post_data.get('phone')
        email = post_data.get('email')
        password = make_password(post_data.get('password'))
        return Customer(first_name=firstname, last_name=lastname, phone=phone, email=email, password=password)


    def __str__(self):
        return self.first_name