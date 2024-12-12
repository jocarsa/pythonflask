from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def inicio():
    return 'Esta es la pagina de inicio'

@aplicacion.route('/sobremi')
def sobremi():
    return 'Esta es la pagina de sobre mi'

@aplicacion.route('/contacto')
def contacto():
    return 'Esta es la pagina de contacto'

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
