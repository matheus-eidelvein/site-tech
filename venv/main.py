from flask import Flask, render_template

app = Flask(__name__)

# Criar a primeira página do site

# route (link) -> site.com/route
# função -> O que você quer exibir naquela página
# template
# Decorator, definir uma nova funcionalidade para a função logo a baixo dela
@app.route("/") # nome_do_site.definir o route dessa página
def paginicial():
    return render_template("paginicial.html")

@app.route("/Contatos")
def contato():
    return render_template("contatos.html")

@app.route("/Usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

# Colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True) # Está ativando o debugar do site, todas as edições feitas no código, tentarão ser exibidas

    # servidor do heroku (deploit - deixar o site online)
