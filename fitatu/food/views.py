from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views.generic import ListView, UpdateView, CreateView
from .forms import DishForm
from .models import Dish


class CreateDish(CreateView):
    template_name = "dish/create.html"
    model = Dish
    fields = ["name", "calories_in_100g"]

    def get_success_url(self):
        return reverse("dishes")


class ListDishes(ListView):
    template_name = "dish/list_dish.html"
    context_object_name = "dishes_list"

    def get_queryset(self):
        return Dish.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ListDishes, self).get_context_data(**kwargs)
        return context


class UpdateDish(UpdateView):
    model = Dish
    fields = ["name"]
    template_name = "dish/update_dish.html"

    def get_success_url(self):
        return reverse("dishes")


def CalculateDishCalories(request, _pk):
    dish = get_object_or_404(Dish, pk=_pk)
    form = DishForm(instance=dish)

    if request.method == "POST":
        form = DishForm(request.POST, instance=dish)
        # value = dish["calories"] * form["portion"]
        form.save()
        print("Calories:", dish.actual_calories)
        return render(request, "dish/calories.html", {"form": form, "model": dish})
    return render(request, "dish/calories.html", {"form": form, "model": dish})
