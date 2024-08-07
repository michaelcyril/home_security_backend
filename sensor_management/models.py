from django.db import models
import uuid


class IntruderAttempt(models.Model):
    STATUS = (
        (0, "OFF"),
        (1, "ON")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pir = models.IntegerField(choices=[(1, 'PIR1'), (2, 'PIR2'), (3, 'PIR3'), (4, 'PIR4')])
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'intruder_attempts'


class Sensor(models.Model):
    STATUS = (
        (0, "OFF"),
        (1, "ON")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pir = models.CharField(max_length=10, choices=[('PIR1', 'PIR1'), ('PIR2', 'PIR2'), ('PIR3', 'PIR3'), ('PIR4', 'PIR4')], unique=True)
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'sensors'


class Alarm(models.Model):
    STATUS = (
        (0, "OFF"),
        (1, "ON")
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.IntegerField(default=0)
    normal_status = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'alarm'


class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    server_ip = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return f'{self.id}'

    class Meta:
        db_table = 'profile'
