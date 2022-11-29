from django.shortcuts import render, redirect
from app.carrito import Carrito
from app.models import Usuario, Autor, Idioma, Editorial, Libro, Detalle
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from datetime import datetime

# inicio


def index(request):
    visitas = request.session.get('visitas', 0)
    if visitas == 0:
        request.session['visitas'] = visitas + 1
        return render(request, 'bienvenida.html')

    return render(request, "index.html")

# logout


def logout_view(request):
    logout(request)
    return redirect("index")

# Registro usuario comun


def registroUsuario(request):
    if request.method == 'POST':
        usuario = Usuario()
        user = User()

        if request.POST["contrasena"] == request.POST["contrasenaConfirm"]:
            usuario.username = request.POST["username"]
            usuario.nombre = request.POST["nombre"]
            usuario.apellido = request.POST["apellido"]
            usuario.rut = request.POST["rut"]
            usuario.direccion = request.POST["direccion"]
            usuario.correo = request.POST["correo"]
            usuario.contrasena = request.POST["contrasena"]

            user.username = request.POST["username"]
            user.first_name = request.POST["nombre"]
            user.last_name = request.POST["apellido"]
            user.email = request.POST["correo"]
            user.is_superuser = 0

            user.password = make_password(request.POST["contrasena"])

            usuario.save()
            user.save()

            return redirect("index")

        else:
            return redirect("signin")

    return render(request, "signin.html")

# Ver autores


def autores(request):
    autores = Autor.objects.all()
    return render(request, "autor.html", {"autores": autores})

# ingresar autores


def ingresarAutores(request):
    if request.method == 'POST':
        autor = Autor()
        autor.nombre = request.POST["nomAutor"]
        autor.apellido = request.POST["apeAutor"]
        autor.url_imagen = request.POST["urlAutor"]
        autor.save()
        return redirect("verAutores")

    return render(request, "autor.html", {"ingresar": "si"})

# eliminar autores


def eliminarAutor(request, id):
    autor = Autor.objects.get(id=id)
    autor.delete()

    return redirect("verAutores")

# editar autores


def editarAutor(request, idAutor):
    if request.method == 'POST':
        autor = Autor(idAutor, request.POST["nomAutor"],
                      request.POST["apeAutor"], request.POST["urlAutor"])
        autor.save()

        return redirect("verAutores")
    else:
        autor = Autor.objects.get(id=idAutor)
        return render(request, "autor.html", {"autor": autor, "editar": "si"})

# ver idiomas


def verIdiomas(request):
    idiomas = Idioma.objects.all()
    return render(request, "idioma.html", {"idiomas": idiomas})

# ingresar idioma


def Ingresaridioma(request):
    if request.method == 'POST':
        idioma = Idioma()
        idioma.nombre = request.POST["nomIdioma"]
        idioma.url_imagen = request.POST["urlIdioma"]
        idioma.save()
        return redirect("verIdiomas")

    return render(request, "idioma.html", {"ingresar": "si"})

# eliminar idioma


def eliminarIdioma(request, id):
    idioma = Idioma.objects.get(id=id)
    idioma.delete()

    return redirect("verIdiomas")

# editar idioma


def editarIdioma(request, idIdioma):
    if request.method == 'POST':
        idioma = Idioma(
            idIdioma, request.POST["nomIdioma"], request.POST["urlIdioma"])
        idioma.save()

        return redirect("verIdiomas")
    else:
        idioma = Idioma.objects.get(id=idIdioma)
        return render(request, "idioma.html", {"idioma": idioma, "editar": 'si'})

# ver editoriales


def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, "editorial.html", {"editoriales": editoriales})

# ingresar editorial


def ingresarEditorial(request):
    if request.method == 'POST':
        editorial = Editorial()
        editorial.nombre = request.POST["nomEditorial"]
        editorial.fono = request.POST["fonEditorial"]
        editorial.correo = request.POST["corEditorial"]
        editorial.pais = request.POST["paiEditorial"]
        editorial.save()
        return redirect("verEditoriales")

    return render(request, "editorial.html", {"ingresar": "si"})

# eliminar editorial


def eliminarEditorial(request, id):
    editorial = Editorial.objects.get(id=id)
    editorial.delete()

    return redirect("verEditoriales")

# editar editorial


def editarEditorial(request, idEditorial):
    if request.method == 'POST':
        editorial = Editorial(idEditorial, request.POST["nomEditorial"], request.POST["fonEditorial"],
                              request.POST["corEditorial"], request.POST["paiEditorial"])
        editorial.save()

        return redirect("verEditoriales")
    else:
        editorial = Editorial.objects.get(id=idEditorial)
        return render(request, "editorial.html", {"editorial": editorial, "editar": "si"})

# ver usuarios


def usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "usuario.html", {"usuarios": usuarios})

# eliminar usuarios


def eliminarUsuario(request, username):
    user = User.objects.get(username=username)
    usuario = Usuario.objects.get(username=username)
    usuario.delete()
    user.delete()

    return redirect("verUsuarios")

# editar usuarios


def editarUsuario(request, user):
    if request.method == 'POST':
        usuario = Usuario(user, request.POST["nomUser"], request.POST["apeUser"], request.POST["rutUser"],
                          request.POST["dirUser"], request.POST["corUser"], request.POST["conUser"])

        user = User.objects.get(username=user)
        user.username = request.POST["username"]
        user.first_name = request.POST["nomUser"]
        user.last_name = request.POST["apeUser"]
        user.email = request.POST["corUser"]
        user.password = make_password(request.POST["conUser"])

        user.save()
        usuario.save()

        return redirect("verUsuarios")
    else:
        usuario = Usuario.objects.get(username=user)
        return render(request, "usuario.html", {"usuario": usuario, "editar": "si"})

# ver libros


def libros(request):
    libros = Libro.objects.all()
    return render(request, "libro.html", {"libros": libros})

# ingresar libros


def ingresarLibro(request):
    if request.method == 'POST':
        libro = Libro()
        libro.titulo = request.POST["titLibro"]
        libro.url_imagen = request.POST["urlLibro"]
        libro.stock = request.POST["stoLibro"]
        libro.anio = request.POST["aniLibro"]
        libro.precio = request.POST["preLibro"]

        libroAut = Autor.objects.get(id=request.POST["autLibro"])
        libro.autor = libroAut

        libroEdit = Editorial.objects.get(id=request.POST["ediLibro"])
        libro.editorial = libroEdit

        libroIdio = Idioma.objects.get(id=request.POST["idiLibro"])
        libro.idioma = libroIdio

        libro.save()
        return redirect("verLibros")

    autorLibros = Autor.objects.all()
    editorialLibros = Editorial.objects.all()
    idiomaLibros = Idioma.objects.all()
    return render(request, "libro.html", {"ingresar": "si", "autorLibros": autorLibros, "editorialLibros": editorialLibros, "idiomaLibros": idiomaLibros})

# eliminar libros


def eliminarLibro(request, id):
    libro = Libro.objects.get(id=id)
    libro.delete()

    return redirect("verLibros")

# editar libros


def editarLibro(request, idLibro):
    if request.method == 'POST':
        libroAut = Autor.objects.get(id=request.POST["autLibro"])
        libroEdit = Editorial.objects.get(id=request.POST["ediLibro"])
        libroIdio = Idioma.objects.get(id=request.POST["idiLibro"])

        libro = Libro(idLibro, request.POST["titLibro"], libroAut, request.POST["urlLibro"], libroEdit,
                      libroIdio,  request.POST["stoLibro"], request.POST["aniLibro"], request.POST["preLibro"])
        libro.save()
        return redirect("verLibros")
    else:
        libro = Libro.objects.get(id=idLibro)
        autorLibros = Autor.objects.all()
        editorialLibros = Editorial.objects.all()
        idiomaLibros = Idioma.objects.all()
        return render(request, "libro.html", {"libro": libro, "editar": "si", "autorLibros": autorLibros, "editorialLibros": editorialLibros, "idiomaLibros": idiomaLibros})

#  pagina de tienda


def tienda(request):
    libros = Libro.objects.all()
    return render(request, "tienda.html", {"libros": libros})

# agregar productos al carro


def agregarCarro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.agregar(libro)
    return redirect("verTienda")

# eliminar el carro


def eliminarCarro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.eliminar(libro)
    return redirect("verTienda")

# restar productos al carro


def restarCarro(request, libro_id):
    carrito = Carrito(request)
    libro = Libro.objects.get(id=libro_id)
    carrito.restar(libro)
    return redirect("verTienda")

# limpiar productos del carro


def limpiarCarro(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("verTienda")

# insertar pedido


def ingresarPedido(request):
    if request.method == 'POST':
        detPed = Detalle()
        detPed.fecha_pedido = datetime.now()
        detPed.precio_total = int(request.POST.get('prePed'))
        detPed.save()

        return redirect("CLS")

    libros = Libro.objects.all()
    return render(request, "tienda.html", {"libros": libros})

# ver pedidos
def pedidos(request):
    detalles = Detalle.objects.all()
    return render(request, "pedidos.html", {"detalles": detalles})

# eliminar pedido
def eliminarPedido(request, id):
    detallePedido = Detalle.objects.get(id = id)
    detallePedido.delete()

    return redirect("verPedidos")
