from flask import Flask

app = Flask(__name__)

#creamos la ruta con sus funciones
@app.route('/')
def holamundo():
    return 'Hola Mundo'

@app.route('/mis-proyectos')
def mis_proyectos():
    return 'Mis proyectos'

if __name__ == '__main__':
    app.run(debug=True)