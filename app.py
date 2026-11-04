from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", titulo="Minha primeira aplicação Flask")


if __name__ == "__main__":
    # host=0.0.0.0 permite o encaminhamento da porta no Codespaces.
    app.run(host="0.0.0.0", port=5000, debug=True)
