from flask import Flask, render_template

app = Flask(__name__)

#creamos la ruta con sus funciones
@app.route('/', methods=['GET'])
def holamundo():
    return render_template('/index.html')

#MIS PROYECTOS
@app.route('/mis-proyectos', methods=['GET'])
def mis_proyectos():
    return render_template('/mis-proyectos.html')

#MI BLOG
@app.route('/blog', methods = ['GET'])
def blog():
    return render_template('/blog.html')

#CONTACTO
@app.route('/contacto', methods = ['GET'])
def contacto():
    return render_template('/contacto.html')


if __name__ == '__main__':
    app.run(debug=True)