from flask import Flask, render_template, request
app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def formulario():
    if request.method == 'POST':
        name = request.form['name']
        dojolocation = request.form['dojolocation']
        options = request.form['options']
        comment = request.form['comment']
        return render_template('resultados.html', name=name, dojolocation=dojolocation, options=options, comment=comment)
    return render_template('formulario.html')
if __name__ == "__main__":
    app.run(debug=True)