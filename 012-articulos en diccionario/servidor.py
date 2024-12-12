from flask import Flask, render_template

aplicacion = Flask(__name__)

mititulo = "La web de Jose Vicente desde Python"
articulos = [
    {
        "titulo":"este es el primer articulo",
        "fecha":"2024-12-12",
        "contenido":"este es el texto del articulo"
     },
    {
        "titulo":"este es el segundo articulo",
        "fecha":"2024-12-13",
        "contenido":"este es el texto del articulo"
     },
     {
        "titulo":"este es el tercer articulo",
        "fecha":"2024-12-14",
        "contenido":"este es el texto del articulo"
     }
]

@aplicacion.route('/')
def inicio():
    return render_template('index.html',titulo=mititulo)

@aplicacion.route('/sobremi')
def sobremi():
    return render_template('sobremi.html',titulo=mititulo)

@aplicacion.route('/contacto')
def contacto():
    return render_template('contacto.html',titulo=mititulo)

@aplicacion.route('/blog')
def blog():
    return render_template('blog.html',titulo=mititulo,articulos=articulos)

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
