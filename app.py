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

@app.route('/cuenta/<cad1>/<cad2>',methods=["GET","POST"])
def contar(cad1,cad2):
    if cad2 == " ":
        abort(404)
    else:
        aparece = cad1.count(cad2)
    return render_template("contar.html",palabra=cad1,letra=cad2,apariciones=aparece)

app.run(debug=True)