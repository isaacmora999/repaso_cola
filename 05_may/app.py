from flask import Flask, render_template, request, redirect, url_for
from banco import Banco


app = Flask(__name__)
banco = Banco()


@app.route('/')
def index():
    Cliente_actual = banco.obtener_ultimo_atendido()
    return render_template('index.html', Cliente_actual=Cliente_actual)

@app.route('/agregar', methods=['post'])
def agregar():
    nombre = request.form.get('nombre')
    if nombre:
        banco.llega_cliente(nombre)
    return redirect(url_for('index'))

@app.route('/atender', methods=['POST'])
def atender():
    banco.atender_cliente()
    return redirect(url_for('index'))   

@app.route('/lista')
def lista():
    clientes = banco.obtener_clientes_en_espera()
    return render_template('lista.html', clientes = clientes) 