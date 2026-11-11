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

@app.route("/dobro/<int:numero>")
def dobro(numero):
    return f"O dobro de {numero} é {numero * 2}"

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/perfil")
def perfil():
    return render_template(
        "perfil.html", nome="Ana", curso="Informática")

@app.route("/nota/<int:nota>")
def nota(nota):
    return render_template("nota.html", nota=nota)

@app.route("/frutas")
def frutas():
    lista = ["Maçã", "Banana", "Caju"]
    return render_template("frutas.html", frutas=lista)



if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
