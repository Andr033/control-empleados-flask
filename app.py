import io
import base64
from flask import Flask, render_template, redirect, request
from empleados import Empleado, db
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import requests

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///basededatos.db"
db.init_app(app)

with app.app_context():
    db.create_all()


respuesta_api = requests.get("https://api.exchangerate-api.com/v4/latest/EUR")
datos_divisas  = respuesta_api.json()
    
@app.route("/")
def inicio():
    # NOMINA TOTAL
    lista = Empleado.query.all()
    nominaTotal = sum(emp.salario for emp in lista)
    
    
    # TOTAL EMPLEADOS
    numeroTotalEmpleados = len(lista) 

    # SALARIO MEDIO
    if numeroTotalEmpleados != 0:
        salarioMedio = nominaTotal / numeroTotalEmpleados
    else:
        salarioMedio = 0
    plot_url_barras = None
    plot_url_tarta = None
    nominas_otras_divisas = {}
    if numeroTotalEmpleados > 0:
    # GRAFICAS
        datos = [{col.name: getattr(emp, col.name) for col in emp.__table__.columns} for emp in lista]
        df = pd.DataFrame(datos)
        resumen = df.groupby("departamento")["salario"].sum()
        
        # Gráfica de barras
        fig1, ax1 = plt.subplots()
        resumen.plot(kind="bar", ax=ax1)
        ax1.set_title("Nómina por departamento")
        ax1.set_xlabel("Departamento")
        ax1.set_ylabel("Nómina")
        fig1.tight_layout()

        img_barras = io.BytesIO()
        fig1.savefig(img_barras, format="png")
        img_barras.seek(0)
        plot_url_barras = base64.b64encode(img_barras.getvalue()).decode("utf-8")
        plt.close(fig1)   # cierra solo esta figura, no todas

        # Gráfica de tarta
        fig2, ax2 = plt.subplots()
        resumen.plot(kind="pie", ax=ax2, autopct="%1.1f%%")
        ax2.set_title("Nómina por departamento")
        fig2.tight_layout()

        img_tarta = io.BytesIO()
        fig2.savefig(img_tarta, format="png")
        img_tarta.seek(0)
        plot_url_tarta = base64.b64encode(img_tarta.getvalue()).decode("utf-8")
        plt.close(fig2)
        
        # Divisas
        
        tasas = datos_divisas.get("rates", {})
        nominas_otras_divisas = {
            "USD": nominaTotal * tasas.get("USD", 1),
            "GBP": nominaTotal * tasas.get("GBP", 1),
            "MXN": nominaTotal * tasas.get("MXN", 1),
            "JPY": nominaTotal * tasas.get("JPY", 1)
        }

    return render_template("index.html", empleados= lista, nominaTotal=nominaTotal, numeroTotalEmpleados=numeroTotalEmpleados, salarioMedio=salarioMedio, plot_url_barras=plot_url_barras, plot_url_tarta=plot_url_tarta, nominas_otras_divisas=nominas_otras_divisas)

@app.route("/nuevo", methods=["GET", "POST"])
def nuevo_empleado():
    if request.method == "POST":
        nombre = request.form["nombre"].lower()
        departamento = request.form["departamento"].lower()
        salario = float(request.form["salario"])
        
        nuevo_empleado = Empleado(
            nombre=nombre,
            departamento=departamento,
            salario=salario
        )
        db.session.add(nuevo_empleado)
        db.session.commit()
        return redirect("/")
    return render_template("nuevo.html")

@app.route("/informe")
def informe():
    lista = Empleado.query.all()
    datos = [{col.name: getattr(emp, col.name) for col in emp.__table__.columns} for emp in lista]
    df = pd.DataFrame(datos)
    with pd.ExcelWriter("informe.xlsx") as writer:
        df.to_excel(writer, sheet_name="Empleados",index=False)
    return redirect("/")


@app.route("/eliminar/<nombre>")
def eliminar(nombre):
    emp = Empleado.query.filter_by(nombre=nombre).first()
    if emp:
        db.session.delete(emp)
        db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)