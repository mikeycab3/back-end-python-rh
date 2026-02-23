import random
from extensions import db

def generar_id():
    while True:
        nuevo_id = random.randint(100000, 999999)
        if not Empleado.query.get(nuevo_id):
            return nuevo_id
        
class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    idEmpleado = db.Column(
        db.Integer,
        primary_key=True,
        default=generar_id   # 👈 aquí se genera automático
    )

    #idEmpleado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    departamento = db.Column(db.String(100), nullable=False)
    sueldo = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f'<Empleado {self.nombre}>'