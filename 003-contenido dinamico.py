from flask import Flask

aplicacion = Flask(__name__)

@aplicacion.route('/')
def inicio():
    cadena = ""
    for dia in range(0,31):
        cadena += str(dia)+"<br>"
    return 'hola mundo desde Python: '+cadena

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
