import os
from models.clases import Cliente, Bodega, Sucursal, Producto, Vendedor, OrdenCompra
from models.exceptionClass import sinStockBodega, cantMaxCarrito, numMinimoCompras

# Bodega
productos = {
    "zapatillas": 20,
    "poleras": 10,
    "zapatos": 15,
    "poleron": 3,
    "chaqueta": 5,
    "guantes": 4
}

# Cliente(run, nombre, apellido, edad, id_usuario, correo, fecha_registro, __saldo)
clientes = [Cliente('111-1', 'Juan', 'Pérez', 30, 1,
                    'jp@gmail.com', '21/03/2022', 50000, 0, 0)]
clientes.append(Cliente('222-2', 'Pedro', 'García', 35,
                2, 'pg@gmail.com', '15/06/2022', 100000, 0, 0))
clientes.append(Cliente('333-3', 'Diego', 'López', 40,
                3, 'dl@gmail.com', '30/09/2022', 75000, 0, 0))
clientes.append(Cliente('444-4', 'Javiera', 'Rodríguez',
                30, 4, 'jr@gmail.com', '02/12/2022', 30000, 0, 0))
clientes.append(Cliente('555-5', 'Francisca', 'Sánchez',
                35, 5, 'fs@gmail.com', '05/02/2023', 90000, 0, 0))

id_compra = 0

bodega1 = Bodega('Calle 1', '999999', 1000)
sucursal1 = Sucursal('Calle2', '99999', 50)
producto1 = Producto(1, 'Arroz', 'Abarrotes', 'Tia Rica', sucursal1, 500, sucursal1.stock)
vendedor1 = Vendedor('222-2', 'Juan', 'Soto', 45, 'Abarrotes', 0, 1)


def nuevo_stock():
    """Agrega un nuevo producto al stock"""
    producto = input("Ingrese el nombre del producto: ")
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        productos[producto] = cantidad
        print(productos)
    except TypeError:
        print("Ingrese un número")


def actualizar_producto():
    """Actualiza el stock de un producto"""
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la cantidad del producto: "))
    productos[producto] += cantidad
    print(productos)


def nombre_productosbodega():
    """Muestra los nombres de los productos en bodega"""
    producto = input("Ingrese el nombre del producto: ")
    if producto in productos:
        print(f'En bodega quedan: {productos[producto]} {producto}')
    else:
        print("El producto no existe")


def todos_productostienda():
    """Muestra todos los productos en la tienda"""
    print('Productos disponibles en la tienda:')
    for producto in productos:
        print(producto)


def productos_enstock():
    """Muestra los productos con stock mayor a 1"""
    stock = "".join(
        f"{producto}, " for producto in productos if productos[producto] >= 1
    )
    print(f'Los productos con stock mayor a 1 es bodega son: {stock}')

    """
    TODO: crear función que calcule el promedio de compras del cliente
    promedio = compras/num_compras. Ambas variables se calculan en el método vender()
    """


def adm_compra():
    """Permite realizar una compra"""
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad > 10:
                raise cantMaxCarrito(cantidad)
            despacho = (input('¿Requiere despacho? (si/no) '))
            id_compra = + 1
            if despacho == 'si':
                OC1 = OrdenCompra(id_compra, producto1, True)
            else:
                OC1 = OrdenCompra(id_compra, producto1, False)
            OC1.vender(clientes[0], cantidad, vendedor1, sucursal1, bodega1, OC1.despacho)
            break
        except sinStockBodega as e:
            print(e)
        except cantMaxCarrito as e:
            print(e)
        except Exception:
            print("La cantidad debe ser un número entero")


def ver_saldo_cliente():
    id_cliente = int(input('Ingrese ID del cliente: '))
    for _ in clientes:
        if id_cliente == _.id:
            return _.saldo


def cambiar_saldo_cliente():
    id_cliente = int(input('Ingrese ID del cliente: '))
    nuevo_saldo = int(input('Ingrese nuevo saldo: '))
    for _ in clientes:
        if id_cliente == _.id:
            _.saldo = nuevo_saldo
            return _.saldo


def mostrar_clientes():
    print('ID   Nombre  Apellido    Correo Electrónico  Fecha de Registro')
    for _ in clientes:
        print(_.id, _.nombre, _.apellido, _.correo, _.fecha)
    print(f'Hay {len(clientes)} usuarios registrados.')


def crear_cliente(nombre, apellido, correo, fecha_registro, saldo_inicial):
    pass


def limpiarTerminal():
    os.system("cls")
