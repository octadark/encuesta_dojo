from flask import render_template, redirect, request
from app_flask import app
from app_flask.modelos.dojo import Dojo

@app.route('/')
def index():
    return render_template("formulario.html")

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    # si hay errores:
    # llamamos al método estático en el modelo Dojo para validar
    if Dojo.is_valid(request.form):
        Dojo.save(request.form)
        # redirigir a la ruta donde se renderiza el formulario de dojo
        return redirect('/resultados')
    # de lo contrario, no hay errores:
    return redirect("/")

@app.route('/resultados')
def results():
    return render_template("resultados.html", dojo = Dojo.get_last_dojo())
