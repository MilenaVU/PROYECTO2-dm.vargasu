from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Especifica la longitud
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def vender(self):
        if self.cantidad > 0:
            self.cantidad -= 1
            db.session.commit()
            return f'Producto {self.nombre} vendido. Cantidad restante: {self.cantidad}'
        else:
            raise ValueError('No hay suficiente cantidad disponible para vender')

class Ingrediente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)  # Especifica la longitud
    cantidad = db.Column(db.Float, nullable=False)

class Receta(db.Model):
    __tablename__ = 'recetas'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)  # Añadir longitud
    descripcion = db.Column(db.Text, nullable=True)
    ingredientes = db.relationship('Ingrediente', secondary='recetas_ingredientes', back_populates='recetas')


class Venta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    producto_id = db.Column(db.Integer, db.ForeignKey('producto.id'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.DateTime, default=db.func.current_timestamp())

    producto = db.relationship('Producto', backref=db.backref('ventas', lazy=True))

class RecetasIngredientes(db.Model):
    __tablename__ = 'recetas_ingredientes'
    receta_id = db.Column(db.Integer, db.ForeignKey('receta.id'), primary_key=True)
    ingrediente_id = db.Column(db.Integer, db.ForeignKey('ingrediente.id'), primary_key=True)
    cantidad = db.Column(db.Float, nullable=False)

    receta = db.relationship('Receta', backref=db.backref('recetas_ingredientes', lazy=True))
    ingrediente = db.relationship('Ingrediente', backref=db.backref('recetas_ingredientes', lazy=True))
