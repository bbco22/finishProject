# Generated by Django 4.1.7 on 2023-04-26 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazin', '0007_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='magazin.tags'),
        ),
    ]