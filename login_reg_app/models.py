from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class UserManager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        if len(post_data["first_name"]) < 2:
            errors["first_name"]= "First name must be at least 2 characters"

        if len(post_data["last_name"]) < 2:
            errors["last_name"]= "Last name must be at least 2 characters"

        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = 'Incorrect Email Address'

        try:
            User.objects.get(email = post_data["email"])
            errors['email_used'] = "Email address already in use."
        except:
            pass

        if len(post_data['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if post_data['password']!= post_data['pw_confirmation']:
            errors['password'] = 'Passwords do not match'

        return errors
    
        

class User(models.Model):
    first_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    email=models.CharField(max_length=80)
    password=models.CharField(max_length=80)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects = UserManager()

