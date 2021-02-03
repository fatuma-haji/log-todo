from django.db import models
from login_reg_app.models import User

class Log(models.Model):
    title= models.CharField(max_length=200)
    complete= models.BooleanField(default=False)
    creator = models.ForeignKey(User, related_name="has_created_list", on_delete=models.CASCADE)
    created_at=models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__ (self):
        return self.title
