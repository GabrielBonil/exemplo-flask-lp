from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pagamentos = [     
    {"texto": "Robert John Downey, Jr", "forma": "Bitcoin", "status":"Pendente"},
    {"texto": "Cris Evans", "forma": "Cheque" , "status":"Pago"},
    {"texto": "Mark Ruffalo", "forma": "Pix", "status":"Pendente" },
    {"texto": "Scarlett Johansson", "forma": "Boleto", "status":"Pago" },
    {"texto": "Jeremy Renner", "forma": "Dinheiro", "status":"Pago" },
    {"texto": "Chris Hemsworth", "forma": "Boleto", "status":"Pendente" },
]

resultados = [
   
]

@app.route('/')
def index():
    return render_template('index.html', lista=pagamentos)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/pesquisa')
def pesquisa():
    return render_template('pesquisa.html')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html', lista2=resultados)

@app.route('/save', methods=['POST'])  # <form action="/save" method="POST">
def save():
    nome = request.form['nome']      # <input name="nome"/>
    forma = request.form['forma']      # <input name="forma"/>
    status = request.form['status']      # <input name="status"/>

    pagamento = { "texto": nome, "forma": forma, "status": status }
    pagamentos.append(pagamento)

    return redirect('https://5000-tan-hedgehog-00ickhj1.ws-us18.gitpod.io/')

@app.route('/del', methods=['POST'])  # <form action="/save" method="POST">
def apagar():
    nome = request.form['nome']      # <input name="nome"/>

    a = 0
    for i in pagamentos:
        print(i["texto"])
        if i["texto"] == nome:
            del pagamentos[a]
        a += 1

    return redirect('https://5000-tan-hedgehog-00ickhj1.ws-us18.gitpod.io/')

@app.route('/busca', methods=['POST'])  # <form action="/save" method="POST">
def busca():
    resultados.clear()
    nome = request.form['nome']      # <input name="nome"/>
    a = 0
    for i in pagamentos:
        if i["texto"] == nome:
            nome = i["texto"]
            forma = i["forma"]
            status = i["status"]

            resultado_pesquisa = { "texto": nome, "forma": forma, "status": status }
            resultados.append(resultado_pesquisa)
        a += 1
    
    return redirect('https://5000-tan-hedgehog-00ickhj1.ws-us18.gitpod.io/resultado')

app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)