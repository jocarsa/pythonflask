from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def inicio():
    return '<h1>Esta es la pagina de inicio</h1>'

@aplicacion.route('/sobremi')
def sobremi():
    return '<h1>Esta es la pagina de sobre mi</h1>'

@aplicacion.route('/contacto')
def contacto():
    return '<h1>Esta es la pagina de contacto</h1>'

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
