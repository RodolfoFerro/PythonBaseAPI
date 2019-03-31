from flask import Flask

app = Flask(__name__)


@app.route('/')
def url_principal():
    return "Hello world!"


@app.route('/pepe/')
def url_pepe():
    return "Hola soy pepe."


if __name__ == '__main__':
    app.run(debug=True, port=5000)
