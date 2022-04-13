from django.test import TestCase

from .models import Dish
from random import randint

# Create your tests here.
class DishModelTests(TestCase):
    def test_was_given_a_negative_mass(self):
        mass = -randint(1, 1000)
        calories = 100
        print(mass)
        negative_mass = Dish(portion=mass, calories_in_100g=calories)
        print(negative_mass)
        self.assertIs(negative_mass.actual_calories, False)
