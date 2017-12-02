from django.db import models
import mongoengine
from mongoengine import *


# Create your models here.
# mongoengine.register_connection(alias="repo",username="htw93_tschueng_wenjun",password="htw93_tscheung_wenjun",name="repo")

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()