from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingrediente(db.Model):
    __tablename__ = 'ingredientes'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cantidad = db.Column(db.Float, nullable=False)
    costo_unitario = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Ingrediente {self.nombre}>'

    def guardar(self):
        db.session.add(self)
        db.session.commit()

    def eliminar(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def obtener_por_id(ingrediente_id):
        return Ingrediente.query.get(ingrediente_id)

    @staticmethod
    def obtener_todos():
        return Ingrediente.query.all()
