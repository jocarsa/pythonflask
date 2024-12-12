from flask import Flask

aplicacion = Flask(__name__)

cabeza = """
    <!doctype html>
    <html>
        <head>
        </head>
        <body>
        <header>
            <h1>La web de Jose Vicente</h1>
            <a href="/">Inicio</a>
            <a href="/sobremi">Sobre mi</a>
            <a href="/contacto">Contacto</a>
        </header>
        <main>
"""

piedepagina = """
    </main>
    </body>
    </html>
"""

@aplicacion.route('/')
def inicio():
    contenido = cabeza + '<h1>Esta es la pagina de inicio</h1>' + piedepagina
    return contenido

@aplicacion.route('/sobremi')
def sobremi():
    contenido = cabeza + '<h1>Esta es la pagina de sobre mi</h1>' + piedepagina
    return contenido

@aplicacion.route('/contacto')
def contacto():
    contenido = cabeza + '<h1>Esta es la pagina de contacto</h1>' + piedepagina
    return contenido

if __name__ == '__main__':
    aplicacion.run(debug=True, port=3000)
