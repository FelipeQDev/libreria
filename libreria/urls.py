from django.contrib import admin
from django.urls import path, include
from app import views as vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vistas.index, name="index"),

    path('accounts/', include('django.contrib.auth.urls')),
    path('signin/', vistas.registroUsuario, name="signin"),
    path('logout/', vistas.logout_view, name="logout"),

    path('autor/', vistas.autores, name="verAutores"),
    path("autor/ingresarAutor/", vistas.ingresarAutores, name="ingresarAutor"),
    path('autor/eliminarAutor/<int:id>', vistas.eliminarAutor, name="eliminarAutor"),
    path('autor/editarAutor/<int:idAutor>', vistas.editarAutor, name="editarAutor"),

    path('idioma', vistas.verIdiomas, name="verIdiomas"),
    path('idioma/ingresarIdioma/', vistas.Ingresaridioma, name="ingresarIdioma"),
    path('idioma/eliminarIdioma/<int:id>', vistas.eliminarIdioma, name="eliminarIdioma"),
    path('idioma/editarIdioma/<int:idIdioma>', vistas.editarIdioma, name="editarIdioma"),

    path('editorial/', vistas.editoriales, name="verEditoriales"),
    path('editorial/ingresarEditorial/', vistas.ingresarEditorial, name="ingresarEditorial"),
    path('editorial/eliminarEditorial/<int:id>', vistas.eliminarEditorial, name="eliminarEditorial"),
    path('editorial/editarEditorial/<int:idEditorial>', vistas.editarEditorial, name="editarEditorial"),

    path('usuario/', vistas.usuarios, name="verUsuarios"),
    path('usuario/eliminarUsuario/<str:username>', vistas.eliminarUsuario, name="eliminarUsuario"),
    path('usuario/editarUsuario/<str:user>', vistas.editarUsuario, name="editarUsuario"),

    path('libro/', vistas.libros, name="verLibros"),
    path('libro/ingresarLibro', vistas.ingresarLibro, name="ingresarLibro"),
    path('libro/eliminarLibro/<int:id>', vistas.eliminarLibro, name="eliminarLibro"),
    path('libro/editarLibro/<int:idLibro>', vistas.editarLibro, name="editarLibro"),

    path('tienda/', vistas.tienda, name="verTienda"),
    path('tienda/agregar/<int:libro_id>/', vistas.agregarCarro, name="Add"),
    path('tienda/eliminar/<int:libro_id>/', vistas.eliminarCarro, name="Del"),
    path('tienda/restar/<int:libro_id>/', vistas.restarCarro, name="Sub"),
    path('tienda/limpiar/', vistas.limpiarCarro, name="CLS"),
    
    path('tienda/ingresarPedido/', vistas.ingresarPedido, name="ingresarPedido"),
    path('pedido/', vistas.pedidos, name="verPedidos"),
    path('pedido/eliminarPedido/<int:id>', vistas.eliminarPedido, name="eliminarPedido")
]
