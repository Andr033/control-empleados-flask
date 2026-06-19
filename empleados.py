from flask_sqlalchemy import SQLAlchemy
from datetime import date

db = SQLAlchemy()

class Empleado(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100))
    salario = db.Column(db.Float)
    incorporacion = db.Column(db.Date, default=date.today)

    def subir_salario(self, porcentaje):

        if self.salario:
            self.salario = self.salario * (1 + porcentaje / 100)
            db.session.commit()