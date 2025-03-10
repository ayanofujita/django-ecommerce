from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttype.models import ContentType
from django.contrib.contenttype.fields import GenericForeignKey

# Create your models here.
class LikedItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    contect_object = GenericForeignKey()
