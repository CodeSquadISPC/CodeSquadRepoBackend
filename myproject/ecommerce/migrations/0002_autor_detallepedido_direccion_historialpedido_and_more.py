# Generated by Django 4.2 on 2024-05-20 20:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id_autor', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'db_table': 'autor',
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id_detalle', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_total', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'verbose_name': 'Detalle de Pedido',
                'verbose_name_plural': 'Detalles de Pedidos',
                'db_table': 'detalle_pedido',
            },
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id_direccion', models.AutoField(primary_key=True, serialize=False)),
                ('direccion', models.TextField()),
                ('ciudad', models.CharField(max_length=255)),
                ('estado', models.CharField(max_length=255)),
                ('codigo_postal', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistorialPedido',
            fields=[
                ('id_historial', models.AutoField(primary_key=True, serialize=False)),
                ('estado_pedido', models.CharField(default='Pendiente', max_length=100)),
                ('fecha_cambio', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LibroAdministrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='LibroAutor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.autor')),
            ],
            options={
                'verbose_name': 'Libro-Autor',
                'verbose_name_plural': 'Libros-Autores',
                'db_table': 'libro_autor',
            },
        ),
        migrations.CreateModel(
            name='Resena',
            fields=[
                ('id_resena', models.AutoField(primary_key=True, serialize=False)),
                ('comentario', models.TextField()),
                ('calificacion', models.IntegerField()),
                ('fecha_resena', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioAdministrador',
            fields=[
                ('id_admin', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=255, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(max_length=254, unique=True)),
                ('contrasena', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioClienteAdministrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuarioadministrador')),
                ('usuario_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuariocliente')),
            ],
            options={
                'unique_together': {('administrador', 'usuario_cliente')},
            },
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='libro',
        ),
        migrations.RemoveField(
            model_name='itempedido',
            name='pedido',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AlterModelOptions(
            name='pedido',
            options={'verbose_name': 'Pedido', 'verbose_name_plural': 'Pedidos'},
        ),
        migrations.RemoveField(
            model_name='libro',
            name='descripcion',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='portada',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido',
            field=models.CharField(default='Pendiente', max_length=100),
        ),
        migrations.AddField(
            model_name='pedido',
            name='fecha_pedido',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.AlterModelTable(
            name='pedido',
            table='pedido',
        ),
        migrations.DeleteModel(
            name='ItemPedido',
        ),
        migrations.AddField(
            model_name='resena',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.libro'),
        ),
        migrations.AddField(
            model_name='resena',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuariocliente'),
        ),
        migrations.AddField(
            model_name='libroautor',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.libro'),
        ),
        migrations.AddField(
            model_name='libroadministrador',
            name='administrador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuarioadministrador'),
        ),
        migrations.AddField(
            model_name='libroadministrador',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.libro'),
        ),
        migrations.AddField(
            model_name='historialpedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.pedido'),
        ),
        migrations.AddField(
            model_name='direccion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuariocliente'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='libro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.libro'),
        ),
        migrations.AddField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.pedido'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ecommerce.usuariocliente'),
        ),
        migrations.AddField(
            model_name='libro',
            name='autor',
            field=models.ManyToManyField(through='ecommerce.LibroAutor', to='ecommerce.autor'),
        ),
        migrations.AlterUniqueTogether(
            name='libroadministrador',
            unique_together={('administrador', 'libro')},
        ),
    ]