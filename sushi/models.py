from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food')
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    composition = models.TextField()

    def __str__(self):
        return self.name


class Portion(models.Model):
    food = models.ManyToManyField(Food, blank=True, related_name='portion')
    price_size30 = models.DecimalField(max_digits=5, decimal_places=0)
    size36 = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)

    def get_food(self):
        return "\n".join([str(p) for p in self.food.all()])
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(args, kwargs)
    #     self.id = None
    #
    # def __int__(self):
    #     return self.id
