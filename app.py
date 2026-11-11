from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Programação Web")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


@app.route("/ola/<nome>")
def ola(nome):
    return render_template("ola.html",nome=nome)

@app.route("/idade/<int:idade>")
def idade(idade):
    return render_template("idade.html",idade=idade)
    
@app.route("/disciplinas")
def disciplinas():
    lista = ["Programação Web" , "Potuguês" ,  "Historia"]
    return render_template("disciplinas.html",disciplinas=lista)

@app.route("/tabuada/<int:n>")
def tabuada(n):
    return render_template("tabuada.html", n=n)
    




if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
