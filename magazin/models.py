from django.db import models
from user.models import User
from django.template.defaultfilters import slugify
from django.core.validators import MinLengthValidator
from django.urls import reverse



def file_path(instance, file_name: str) -> str:

    # "Название класса (lower)" / "name" / "file_name"
    return "/".join([instance.__class__.__name__.lower(), instance.slug, file_name])

# Класс категорий
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to=file_path)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("items_list",
                        args=[self.slug])


# Класс товаров
class Product(models.Model):

    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True)
    cost = models.IntegerField()
    count = models.PositiveIntegerField()
    about = models.TextField()
    available = models.BooleanField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(max_length=100, blank=True, unique=True)
    image = models.ImageField(upload_to=file_path)



    class Meta:
        ordering = ("name",)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_item",
                        args=[self.slug, self.id]
                       )

class Tags(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

