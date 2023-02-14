from flask import Flask, render_template

app = Flask("__name__")

# POSTS MOCK
posts = [
    { 
        "titulo": "Post 1",
        "texto": "meu primeiro post"
    },
    {
        "titulo": "Post 2",
        "texto": "meu sgundo post"
    }
]

@app.route('/')
def exbir_entradas():
    return render_template("exibir_entradas.html", entradas=posts)

@app.route('/pudim')
def pudim():
    return "eu gosto de pudim de morango"
