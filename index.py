from flask import Flask,render_template

#Constante do meu Site
CONST_SITE = {
    "NAME" : "Galeria Awesome",    
    "LOGO": "/static/img/logo_galeria.png",
    "CR":"&copy; 2024 Minha Galeria de Fotos",
}


app = Flask(__name__)


@app.route("/")
def home():
    toPage = {
        "site": CONST_SITE,
        "title": "Página Inical",
        "css":"home.css",
    }
    return render_template("home.html", page=toPage)


@app.route("/contacts")
def contact():
    return "Contato"

@app.route("/about")
def about():
    return "Quem somos"

@app.route("/policies")
def policies():
    return "Políticas de privacidade"

@app.route("/gallery")
def gallery():
   return "Era para ter uma imagem aqui. :/"


@app.errorhandler(404)
def errors(e):
    return "Página não encontrada."


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True)  # Altere 5001 para a porta desejada