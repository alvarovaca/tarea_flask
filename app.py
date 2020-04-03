from flask import Flask, render_template, abort
from lxml import etree
app = Flask (__name__)

@app.route('/')
def inicio():
    return render_template("inicio.html")

@app.route('/potencia/<int:base>/<int:exponente>',methods=["GET","POST"])
def potencia(base,exponente):
    if exponente > 0:
        resultado = base**exponente
    elif exponente == 0:
        resultado = 1
    elif exponente < 0:
        resultado = 1/(base**abs(exponente))
    return render_template("potencia.html",ba=base,ex=exponente,res=resultado)

app.run(debug=True)