# Generated by Django 5.0.4 on 2024-05-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0011_rol'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rol',
            name='nombre_rol',
        ),
        migrations.AddField(
            model_name='rol',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rol',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
