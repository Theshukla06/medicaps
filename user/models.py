import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from user.managers import UserManager

class BaseModel(models.Model):
    id = models.UUIDField(primary_key = True, editable = False, default = uuid.uuid4)

    class Meta:
        abstract = True



class User(AbstractUser, BaseModel):
    username = None
    full_name = models.CharField(max_length = 200)
    email = models.EmailField(unique = True, max_length = 100)
    mobile_no = models.CharField(max_length = 15)

    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    # def get_full_name(self):
    #     return self.full_name.strip()

    def save(self, *args, **kwargs):
        if not self.full_name:
            self.full_name = f"{self.first_name} {self.last_name}".strip()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

