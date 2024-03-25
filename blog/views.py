from django.shortcuts import render

from .models import General, Materia, Etiqueta, Post

# Create your views here.

def Index(request):

    info= General.objects.all()
    materias = Materia.objects.all()
    etiquetas = Etiqueta.objects.all()

    for i in range(len(info)):
        nombre = info[i].nombre
        creador = info[i].creador
        tiktok= info[i].tiktok
        facebook= info[i].facebook 
        correo= info[i].correo 
        descripcion = info[i].descripcion

    context = {
        'nombre':nombre,
        'creador':creador,
        'tiktok':tiktok,
        'facebook':facebook,
        'correo':correo,
        'descripcion':descripcion,

        'materias':materias,
        'etiquetas':etiquetas,
    }

    return render(request, 'index.html', context)

def Blog(request):
    info= General.objects.all()

    for i in range(len(info)):
        nombre = info[i].nombre
        creador = info[i].creador
        tiktok= info[i].tiktok
        facebook= info[i].facebook 
        correo= info[i].correo

    q1 = request.GET.get('q1')
    q2 = request.GET.get('q2')

    id = 0

    if q1=='materia':
        materia = Materia.objects.filter(materia=q2)

        for i in range(len(materia)):
            id = materia[i].id 

        posts = Post.objects.filter(materia=id)
    elif q1=='etiqueta':
        etiqueta = Etiqueta.objects.filter(etiqueta=q2)

        for i in range(len(etiqueta)):
            id = etiqueta[i].id 

        posts = Post.objects.filter(etiqueta=id)
    else:
        q2= 'Todo'
        posts = Post.objects.all()

    contador = posts.count()

    #print(contador)
    
    context = {
        'nombre':nombre,
        'creador':creador,
        'tiktok':tiktok,
        'facebook':facebook,
        'correo':correo,

        'tema':q2,
        'contador': contador,

        'posts':posts,
    }

    #print(q1,q2)

    return render(request, 'blog.html', context)

def PostDetail(request, pk):

    post = Post.objects.filter(id=pk)

    for i in range(len(post)):
        titulo= post[i].titulo
        subtitulo= post[i].subtitulo
        creacion= post[i].creacion
        autor= post[i].autor
        cuerpo= post[i].body
        materia= post[i].materia
        etiqueta= post[i].etiqueta

    context={
        'titulo':titulo,
        'subtitulo':subtitulo,
        'creacion':creacion,
        'autor':autor,
        'cuerpo':cuerpo,
        'materia':materia,
        'etiqueta':etiqueta,
    }

    return render(request, 'post.html', context)
