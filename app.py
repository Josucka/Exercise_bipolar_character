from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def home():
    nome = "Ravena"
    exibir_imagem = True
    gif_1 = "https://th.bing.com/th/id/R6acc8390d31904543ce26bad9b0e31dc?rik=dlfxcONjyXVPcQ&pid=ImgRaw"
    return render_template(
        "index.html",
        nome = nome,
        exibir_imagem = exibir_imagem,
        gif_1 = gif_1,
    )
@app.route('/chateada')
def chateada():
    nome = "Ravena"
    exibir_imagem = True
    gif_2 = "https://th.bing.com/th/id/Rcd125841ddb30e99f3371e357a21e61c?rik=SrcYTKZsYrM37w&pid=ImgRaw"
    return render_template(
        "index.html",
        nome = nome,
        exibir_imagem = exibir_imagem,
        gif_2 = gif_2
    )
if __name__ == "__main__":
    app.run(debug=True)
