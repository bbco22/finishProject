# Generated by Django 4.1.7 on 2023-04-20 10:02

from django.db import migrations, models
import django.db.models.deletion
import magazin.models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0004_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('cost', models.IntegerField()),
                ('count', models.PositiveIntegerField()),
                ('about', models.TextField()),
                ('available', models.BooleanField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
                ('image', models.ImageField(upload_to=magazin.models.file_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='magazin.category')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.RemoveField(
            model_name='makeup',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='toys',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='vitamins',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
        migrations.DeleteModel(
            name='Toys',
        ),
        migrations.DeleteModel(
            name='Vitamins',
        ),
        migrations.AlterField(
            model_name='orders',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='magazin.product'),
        ),
        migrations.DeleteModel(
            name='Makeup',
        ),
    ]
