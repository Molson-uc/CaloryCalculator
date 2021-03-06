from django.db import models
from django.urls import reverse
from django.shortcuts import redirect


class Dish(models.Model):
    name = models.CharField(max_length=100)
    portion = models.IntegerField(default=100)
    calories_in_100g = models.IntegerField()
    # actual_calories = models.IntegerField()

    def get_absolute_url(self):
        return reverse("detail-dish", kwargs={"pk": self.pk})


