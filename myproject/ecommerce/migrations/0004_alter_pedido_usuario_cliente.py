# Generated by Django 4.2 on 2024-05-21 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0003_formaenvio_formapago_rename_resena_reseña_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='usuario_cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuariocliente'),
        ),
    ]
