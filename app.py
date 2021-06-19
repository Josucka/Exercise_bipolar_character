from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    nome = "Ravena"
    humor = "Feliz"
    botao = "avancar"
    exibir_imagem = True
    gif = "https://th.bing.com/th/id/R6acc8390d31904543ce26bad9b0e31dc?rik=dlfxcONjyXVPcQ&pid=ImgRaw"
    return render_template(
        "index.html",
        nome = nome,
        humor = humor,
        botao = botao,
        exibir_imagem = exibir_imagem,
        gif = gif,
    )
@app.route('/chateada')
def chateada():
    nome = "Ravena"
    humor = "nao tao feliz"
    botao = "voltar"
    exibir_imagem = True
    gif = "https://th.bing.com/th/id/Rcd125841ddb30e99f3371e357a21e61c?rik=SrcYTKZsYrM37w&pid=ImgRaw"
    return render_template(
        "index.html",
        nome = nome,
        humor = humor,
        botao = botao, #tenho que rever esse botao que nao ta voltando
        exibir_imagem = exibir_imagem,
        gif = gif
    )
if __name__ == "__main__":
    app.run(debug=True)