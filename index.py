from flask import Flask, render_template

# Constante do meu Site
# Define um dicionário com informações do site, como nome, logo, direitos autorais,
# links de CSS e JS, menu, redes sociais e links úteis.
CONST_SITE = {
    "NAME": "Galeria Awesome",  # Nome do site
    "LOGO": "/static/img/logo_galeria.png",  # Caminho para o logo do site
    "CR": "&copy; 2024 Minha Galeria de Fotos",  # Direitos autorais
    "css": "/static/css/template.css",  # Caminho para o arquivo CSS principal
    "js": "/static/js/template.js",  # Caminho para o arquivo JS principal
    "toogle": '''  
                <span id="toogleMenu"> 
                <i class="fa-solid fa-bars fa-fw"></i> 
                </span> 
                ''',  # HTML para o botão de alternar o menu
    "menu": {  # Dicionário para os links do menu
        "home": '''  
                <a href="/" title="Página inicial"> 
                    <i class="fa-solid fa-camera fa-fw"></i>  
                    <span>Inicio</span> 
                </a> 
                ''',  # Link para a página inicial
        "galeria": '''  
                    <a href="/galeria" title="Galeria de Iamgens">
                        <i class="fa-solid fa-images fa-fw"></i>
                        <span>Galeria</span> 
                    </a>
                    ''',  # Link para a galeria de imagens
        "contato": '''  
                    <a href="/contacts" title="Contatos">
                        <i class="fa-solid fa-address-book fa-fw"></i>
                        <span>Contatos</span>
                    </a>
                ''',  # Link para a página de contato
        "sobre": '''  
                    <a href="/about" title="Informações sobre quem somos">
                        <i class="fa-solid fa-circle-info fa-fw"></i>
                        <span>Sobre</span>
                    </a>
                '''  # Link para a página sobre
    },
    "redesSociais": {  # Dicionário para os links das redes sociais
        "facebook": '''  
                    <a href="https://facebook.com" target="_blank" rel="noopener">
                            <i class="fa-brands fa-facebook fa-fw"></i>
                            <span>Facebook</span>
                    </a>
                ''',  # Link para o Facebook
        "x": '''  
            <a href="https://x.com" target="_blank" rel="noopener">
                <i class="fa-brands fa-x-twitter fa-fw"></i>
                <span>Twitter</span>
            </a>
        ''',  # Link para o Twitter (antigo X)
        "github": '''  
                <a href="https://github.com" target="_blank" rel="noopener">
                    <i class="fa-brands fa-github fa-fw"></i>
                    <span>Github</span>
                </a>
        '''  # Link para o GitHub
    },
    "links": {  # Dicionário para links adicionais
        "politica": '''  
                    <a href="/policies">
                        <i class="fa-solid fa-book fa-fw"></i>
                        <span>Políticas</span>
                    </a>
                '''  # Link para a política de privacidade
    }
}

# Criação da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial


@app.route("/")
def home():
    toPage = {  # Dicionário com informações para a página inicial
        "site": CONST_SITE,  # Passa as informações do site
        "title": "Página Inicial",  # Título da página
        "css": "home.css",  # Arquivo CSS específico da página
    }
    # Renderiza o template home.html
    return render_template("home.html", page=toPage)

# Rota para a página de contato
@app.route("/contacts")
def contact():
    toPage = {
        "site": CONST_SITE,
        "title": "Faça contato",
        "css": "contacts.css",
    }
    # Renderiza o template contacts.html
    return render_template("contacts.html", page=toPage)

# Rota para a página "Sobre"
@app.route("/about")
def about():
    toPage = {
        "site": CONST_SITE,
        "title": "Quem somos",
        "css": "about.css",
    }
    # Renderiza o template about.html
    return render_template("about.html", page=toPage)

# Rota para a política de privacidade
@app.route("/policies")
def policies():
    toPage = {
        "site": CONST_SITE,
        "title": "Política de Privacidade",
        "css": "policies.css",
    }
    # Renderiza o template policies.html
    return render_template("policies.html", page=toPage)

# Rota para a galeria de fotos
@app.route("/galeria")
def galeria():
    toPage = {
        "site": CONST_SITE,
        "title": "Galeria de Fotos",
        "css": "galeria.css",
    }
    # Renderiza o template galeria.html
    return render_template("galeria.html", page=toPage)

# Tratamento de erros 404 (página não encontrada)
@app.errorhandler(404)
def errors(e):
    return "Página não encontrada."  # Mensagem de erro


# Executa a aplicação
if __name__ == "__main__":
    # app.run(debug=True)  # Para desenvolvimento, habilita o modo debug
    app.run(debug=True)  # Executa a aplicação na porta padrão (5000)
