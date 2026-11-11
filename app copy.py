from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="index.html")

@app.route("/ajuda")
def ajuda():
    return "página de ajuda"

@app.route("/contato")
def contato():
    return "página de contato"

@app.route("/ola/ <nome>")
def ola(nome):
    return f"olá, {nome}!"


if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
