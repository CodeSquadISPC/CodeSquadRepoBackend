from django.contrib import admin
from .models import (Categoria, Autor, UsuarioCliente, UsuarioAdministrador, 
                     Direccion, FormaEnvio, FormaPago, Pedido, HistorialPedido, 
                     Reseña, Libro, DetallePedido, Rol)


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('rol', 'description')
    search_fields = ('rol',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_categoria')
    search_fields = ('nombre_categoria',)

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('id_autor', 'nombre')
    search_fields = ('nombre',)

@admin.register(UsuarioCliente)
class UsuarioClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(UsuarioAdministrador)
class UsuarioAdministradorAdmin(admin.ModelAdmin):
    list_display = ('id_admin', 'usuario')
    search_fields = ('usuario',)

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ('direccion', 'ciudad', 'provincia', 'codigo_postal')
    search_fields = ('direccion', 'ciudad', 'provincia', 'codigo_postal')

@admin.register(FormaEnvio)
class FormaEnvioAdmin(admin.ModelAdmin):
    list_display = ('id_forma_envio', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(FormaPago)
class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('id_forma_pago', 'descripcion')
    search_fields = ('descripcion',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'usuario_cliente', 'estado_pedido', 'fecha_pedido', 'direccion_envio', 'forma_envio', 'forma_pago')
    search_fields = ('usuario_cliente__nombre', 'estado_pedido')
    list_filter = ('estado_pedido', 'fecha_pedido', 'forma_envio', 'forma_pago')

@admin.register(HistorialPedido)
class HistorialPedidoAdmin(admin.ModelAdmin):
    list_display = ('id_historial', 'pedido', 'estado_pedido', 'fecha_cambio')
    search_fields = ('pedido__id_pedido', 'estado_pedido')
    list_filter = ('estado_pedido', 'fecha_cambio')

@admin.register(Reseña)
class ResenaAdmin(admin.ModelAdmin):
    list_display = ('id_resena', 'libro', 'usuario_cliente', 'comentario', 'calificacion', 'fecha_resena')
    search_fields = ('libro__titulo', 'usuario_cliente__nombre', 'calificacion')
    list_filter = ('calificacion', 'fecha_resena')

@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('id_libro', 'titulo', 'portada', 'categoria', 'autor', 'descripcion', 'precio', 'stock')
    search_fields = ('titulo', 'precio')
    list_filter = ('categoria',)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('id_detalle', 'pedido', 'libro', 'cantidad', 'precio_unitario', 'precio_total')
    search_fields = ('pedido__id_pedido', 'libro__titulo')
    list_filter = ('pedido',)

