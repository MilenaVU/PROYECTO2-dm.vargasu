# tests/test_models.py

import pytest
from models.models import Producto, Ingrediente, Receta, Venta

def test_producto_creation(init_db):
    producto = Producto(nombre='Helado', precio=5.99, stock=10)
    init_db.session.add(producto)
    init_db.session.commit()

    assert producto.id is not None
    assert producto.nombre == 'Helado'
    assert producto.precio == 5.99
    assert producto.stock == 10

def test_ingrediente_creation(init_db):
    ingrediente = Ingrediente(nombre='Chocolate', cantidad=50.0)
    init_db.session.add(ingrediente)
    init_db.session.commit()

    assert ingrediente.id is not None
    assert ingrediente.nombre == 'Chocolate'
    assert ingrediente.cantidad == 50.0

def test_receta_creation(init_db):
    ingrediente = Ingrediente(nombre='Chocolate', cantidad=50.0)
    init_db.session.add(ingrediente)
    init_db.session.commit()

    receta = Receta(nombre='Helado de Chocolate', descripcion='Un delicioso helado de chocolate.')
    receta.ingredientes.append(ingrediente)
    init_db.session.add(receta)
    init_db.session.commit()

    assert receta.id is not None
    assert receta.nombre == 'Helado de Chocolate'
    assert len(receta.ingredientes) == 1
    assert receta.ingredientes[0].nombre == 'Chocolate'

def test_venta_creation(init_db):
    producto = Producto(nombre='Helado', precio=5.99, stock=10)
    init_db.session.add(producto)
    init_db.session.commit()

    venta = Venta(producto_id=producto.id, cantidad=2)
    init_db.session.add(venta)
    init_db.session.commit()

    assert venta.id is not None
    assert venta.producto_id == producto.id
    assert venta.cantidad == 2
