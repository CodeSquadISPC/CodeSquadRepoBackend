# Generated by Django 5.0.4 on 2024-05-27 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0013_alter_rol_description_alter_rol_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarioadministrador',
            name='roles',
            field=models.ManyToManyField(to='ecommerce.rol'),
        ),
        migrations.AddField(
            model_name='usuariocliente',
            name='roles',
            field=models.ManyToManyField(to='ecommerce.rol'),
        ),
    ]