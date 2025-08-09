from django.db import models
from django.db.models import ForeignKey
from django.db.models.fields import CharField, TextField, EmailField


class Race(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(blank=True)


class Skill(models.Model):
    name = CharField(max_length=255, unique=True)
    bonus = CharField(max_length=255)
    race = ForeignKey(Race, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"name: {self.name}"


class Guild(models.Model):
    name = CharField(max_length=255, unique=True)
    description = TextField(null=True)


class Player(models.Model):
    nickname = CharField(max_length=255, unique=True)
    email = EmailField(max_length=255)
    bio = CharField(
        max_length=255,
        help_text="It stores a short description "
                  "provided by a user about himself/herself."
    )
    race = ForeignKey(Race, on_delete=models.CASCADE)
    guild = ForeignKey(
        Guild, to_field="id",
        on_delete=models.SET_NULL,
        null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
