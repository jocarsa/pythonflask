from flask import Flask, render_template
import json

aplicacion = Flask(__name__)

mititulo = "La web de Jose Vicente desde Python"



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
    archivo = open("basededatos/articulos.json",'r')
    articulos = json.load(archivo)
    archivo.close()
    return render_template('blog.html',titulo=mititulo,articulos=articulos)

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
