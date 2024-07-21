from flask import render_template, request, redirect, url_for
from app import app, db
from models.models import Ingrediente, Producto

# Rutas y controladores aquí

# Ejemplo de ruta para mostrar el menú de la heladería
@app.route('/')
def mostrar_menu():
    productos = Producto.query.all()
    return render_template('index.html', productos=productos)

# Más rutas y controladores según necesidades
