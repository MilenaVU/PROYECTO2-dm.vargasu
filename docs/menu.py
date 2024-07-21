
from base import Base
from complemento import Complemento
from copa import Copa
from malteada import Malteada
from heladeria import Heladeria

def main():
    # Crear ingredientes
    helado_fresa = Base("Helado de Fresa", 1200, 80, 10, True, "Fresa")
    chispas_chocolate = Complemento("Chispas de chocolate", 500, 150, 20, False)
    mani = Complemento("Mani ", 900, 200, 15, False)

    # Crear productos
    copa = Copa("Samurai de fresas", 7500, "Grande", [helado_fresa, chispas_chocolate, mani])
    malteada = Malteada("Malteada chocoespacial", 8500, 16, [helado_fresa, chispas_chocolate, mani])

    # Crear heladería
    heladeria = Heladeria()
    heladeria.agregar_ingrediente(helado_fresa)
    heladeria.agregar_ingrediente(chispas_chocolate)
    heladeria.agregar_ingrediente(mani)

    heladeria.agregar_producto(copa)
    heladeria.agregar_producto(malteada)

    # Probar la función de vender
    print("Intentando vender 'Samurai de fresas'...")
    if heladeria.vender("Samurai de fresas"):
        print("Venta exitosa!")
    else:
        print("No se pudo realizar la venta.")

    print("Intentando vender 'Malteada chocoespacial'...")
    if heladeria.vender("Malteada chocoespacial"):
        print("Venta exitosa!")
    else:
        print("No se pudo realizar la venta.")

    # Mostrar el producto más rentable
    print("Producto más rentable:", heladeria.producto_mas_rentable())

if __name__ == "__main__":
    main()
