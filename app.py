from flask import Flask, render_template
from flask_migrate import Migrate
from models.models import db, Producto, Ingrediente, Receta, Venta, RecetasIngredientes

def create_app():
    app = Flask(__name__)

    # Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Ch*col4t3.@localhost/heladeria_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicialización de SQLAlchemy con la app
    db.init_app(app)

    # Inicialización de Flask-Migrate
    migrate = Migrate(app, db)

    # Rutas y lógica de la aplicación
    @app.route('/')
    def index():
        productos = Producto.query.all()
        return render_template('index.html', productos=productos)

    @app.route('/vender/<int:producto_id>')
    def vender_producto(producto_id):
        try:
            producto = Producto.query.get(producto_id)
            mensaje = producto.vender()
            return mensaje
        except ValueError as e:
            return str(e)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
