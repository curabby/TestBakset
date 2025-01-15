import uuid

from django.db import models

# Create your models here.
"""
Объект VPS должен включать следующие параметры:
uid — уникальный идентификатор сервера.
cpu — количество процессорных ядер.
ram — объем оперативной памяти.
hdd — объем дискового пространства.
status — текущий статус сервера (например, started, blocked, stopped).
"""
class VPS(models.Model):
    STATUS_CHOICES = [
        ('started', 'Started'),
        ('blocked', 'Blocked'),
        ('stopped', 'Stopped'),
        ('restarted', 'Restarted'),
    ]

    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu = models.IntegerField(default=1)
    ram = models.IntegerField(default=1)
    hdd = models.IntegerField(default=10)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='started')

    def __str__(self):
        return f"VPS {self.uid} - Status: {self.get_status_display()}"
