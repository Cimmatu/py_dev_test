import uuid
from django.db import models

# Create your models here.


class Request(models.Model):
    ON_PENDING = 'on_pending'
    CONSIDERED = 'considered'
    CLOSED = 'closed'
    STATUS = (
        (ON_PENDING, 'Your request is pending'),
        (CONSIDERED, 'Your request is being considered'),
        (CLOSED, 'Your request closed'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)#нельзя редактировать вручную
    status = models.CharField(choices=STATUS, default=ON_PENDING)
    description = models.TextField()


class Offer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creation_date = models.DateTimeField()
    description = models.TextField(max_length=200)
    price = models.FloatField()
    request_id = models.ForeignKey(Request, on_delete=models.CASCADE)


class Profile(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.CharField()
    admin_status = models.BooleanField()

