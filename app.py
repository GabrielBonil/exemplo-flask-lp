from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

pagamentos = []

resultados = []

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

    return redirect('https://5000-aqua-meerkat-684qbl2o.ws-us17.gitpod.io/')

@app.route('/del', methods=['POST'])  # <form action="/save" method="POST">
def apagar():
    nome = request.form['nome']      # <input name="nome"/>
    numero = 0
    i1 = 0

    for i in pagamentos:
        numero += 1

    for i in range(numero):
        if pagamentos[i1]["texto"].lower() == nome.lower():
            del pagamentos[i1]
            i1 -= 1
        i1 += 1

    return redirect('https://5000-aqua-meerkat-684qbl2o.ws-us17.gitpod.io/')

@app.route('/busca', methods=['POST'])  # <form action="/save" method="POST">
def busca():
    resultados.clear()
    nome2 = request.form['nome']      # <input name="nome"/>
    a = 0
    for i in pagamentos:
        if nome2.lower() in i["texto"].lower():
            nome = i["texto"]
            forma = i["forma"]
            status = i["status"]

            resultado_pesquisa = { "texto": nome, "forma": forma, "status": status }
            resultados.append(resultado_pesquisa)
        a += 1
    
    return redirect('https://5000-aqua-meerkat-684qbl2o.ws-us17.gitpod.io/resultado')

app.run(debug=True)


# Implementar o DELETE!! (2,0 pontos)
# Implementar uma pesquisa (3,0 pontos)