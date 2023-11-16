from django.db import models
from django.contrib.auth.models import User

# Create user and save to the database
user = User.objects.create_user('myusername', 'mypassword')

# Update fields and then save again
user.first_name = 'Chris'
user.last_name = 'Nolan'
user.save()
# Create your models here.
