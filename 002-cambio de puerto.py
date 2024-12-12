from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def inicio():
    return 'hola mundo desde Python'

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
