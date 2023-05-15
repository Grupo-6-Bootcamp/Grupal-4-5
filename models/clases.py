class Persona:
    def __init__(self, run, nombre, apellido, edad):
        self.run = run
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

class Cliente(Persona):
    def __init__(self, run, nombre, apellido, edad, id_usuario, correo, fecha_registro, __saldo):
        super().__init__(run, nombre, apellido, edad)
        self.id = id_usuario
        self.correo = correo
        self.fecha = fecha_registro
        self.__saldo = __saldo
        self.impuesto = 1.19

    @property
    def saldo(self):
        """Obtiene el saldo del cliente"""
        return (self.__saldo)

    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo

    def obtenerCliente(self, id):
        return self.nombre if id == self.id else None

class Edificio:
    def __init__(self, direccion, telefono):
        self.direccion = direccion
        self.telefono = telefono

class Sucursal(Edificio):
    def __init__(self, direccion, telefono, stock):
        super().__init__(direccion, telefono)
        self.stock = stock
    
    def reponerStock(self, cantidad, bodega):
        if bodega.stock <= cantidad:
            print('No existe stock suficiente para reponer')
        else:
            self.stock += cantidad
            bodega.stock -= cantidad
            print('El stock del producto en la sucursal no es suficiente.')
            print(f'Se está solicitando y reponiendo {cantidad} productos a Bodega...')
            print(f'El nuevo stock del producto es de {self.stock} unidades \n')
    
    def requiereStock(self, cantidad, bodega):
        if self.stock < 50:
            self.reponerStock(cantidad, bodega)
            print(f'Se está solicitando y reponiendo {cantidad} productos...')
    
class Bodega(Edificio):
    def __init__(self, direccion, telefono, stock):
        super().__init__(direccion, telefono)
        self.stock = stock

class CategoriaProducto:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

class Producto:
    categoria: CategoriaProducto
    sucursal: Sucursal

    def __init__(self, sku, nombre, categoria, proveedor, sucursal, valor_neto, *prioritario):
        self.sku = sku
        self.nombre = nombre
        self.categoria = categoria
        self.proveedor = proveedor
        self.sucursal = sucursal
        self.valor_neto = valor_neto
        self.prioritario = prioritario[0] if prioritario else False

    def comisionPrioritario(self, cantidad) -> float:
        if self.prioritario is False:
            return self.valor_neto * cantidad * 0.005
        return self.valor_neto * cantidad * 0.01

    def cambiarValorProducto(self, nuevo_valor):
        self.valor_neto = nuevo_valor
        print(
            f'El valor del producto {self.nombre} fue cambiado a ${self.valor_neto}')

class Vendedor(Persona):
    def __init__(self, run, nombre, apellido, edad, seccion, __comision, ventas):
        super().__init__(run, nombre, apellido, edad)
        self.seccion = seccion
        self.__comision = __comision
        self.ventas = 0

    @property
    def comision(self):
        """Obtiene la comisión por defecto del vendedor"""
        return (self.__comision)

    @comision.setter
    def comision(self, comision):
        self.__comision = comision

    def consultarVentas(self):
        print(f'Las ventas del vendedor {self.nombre} son ${self.ventas}')

class Proveedor:
    def __init__(self, rut, nombre_legal, razon_social, pais, es_persona_juridica):
        self.rut = rut
        self.nombre_legal = nombre_legal
        self.razon_social = razon_social
        self.pais = pais
        self.es_persona_juridica = True

    def agregarStockProducto(self, producto, cantidad):
        producto.stock += cantidad
        print(
            f'Se agregaron {cantidad} unidades al producto {producto.nombre}')

class OrdenCompra:
    producto: Producto
    id_compra = 1
    
    def __init__(self, id_compra, producto, despacho):
        self.id_compra = id_compra
        self.producto = producto
        self.despacho = despacho

    def generaOC(self, id_compra, producto, cantidad, despacho):
        id_compra += 1
        if despacho:
            self.OC_basica(id_compra, producto, cantidad)
            valor_total = producto.valor_neto * cantidad * 1.19 + 5000
            print('Valor despacho: $5000')
            print(f'Valor Total: {valor_total}')
        else:
            self.OC_basica(id_compra, producto, cantidad)
            print(f'Valor Total: {producto.valor_neto * cantidad * 1.19}')

    def OC_basica(self, id_compra, producto, cantidad):
        print(f'Orden de Compra N° {id_compra}:')
        print(f'Cantidad: {cantidad} unidades')
        print(f'Valor neto: ${producto.valor_neto * cantidad}')
        print(f'Impuesto: ${producto.valor_neto * cantidad * 0.19}')

    def vender(self, cliente, cantidad, vendedor, sucursal, bodega, despacho):
        # sourcery skip: extract-method
        if self.producto.sucursal.stock < cantidad:
            sucursal.reponerStock(300, bodega)
        if cliente.saldo >= self.producto.valor_neto * cantidad:
            self.producto.sucursal.stock -= cantidad
            vendedor.comision += self.producto.comisionPrioritario(cantidad)
            if despacho:
                cliente.saldo -= self.producto.valor_neto * cantidad * 1.19 + 5000
            else:
                cliente.saldo -= self.producto.valor_neto * cantidad * 1.19
            vendedor.ventas += self.producto.valor_neto * cantidad
            self.generaOC(self.id_compra, self.producto, cantidad, self.despacho)
            print(
                f'El producto {self.producto.nombre} fue vendido exitosamente, el saldo del cliente es {cliente.saldo}')
            print(f'El nuevo stock del producto {self.producto.nombre} es de {self.producto.sucursal.stock} unidades.')
        else:
            print(
                f'El cliente {cliente.nombre} {cliente.apellido} no tiene saldo suficiente para comprar el producto {self.producto.nombre}')
            # print(f'El producto {self.producto.nombre} no tiene stock disponible')

class Factura:
    def __init__(self, id_factura, glosa, valor_total):
        self.id_factura = id_factura
        self.glosa = glosa
        self.valor_total = valor_total

    def emitirFactura(self, venta):
        pass

# bodega1 = Bodega('Calle 1', '999999', 1500)
# sucursal1 = Sucursal('Calle2', '99999', 50)

# sucursal1.stock = 40
# sucursal1.requiereStock(300, bodega1)
# print(sucursal1.stock)

# cliente1 = Cliente('111-1', 'Juan', 'Perez', 30, 1, 'juan@juan.com', '2020-01-01', 1000000)
# vendedor1 = Vendedor('222-2', 'Juan', 'Soto', 45, 'Abarrotes', 0, 1)

# producto1 = Producto(1, 'Arroz', 'Abarrotes', 'Tia Rica', sucursal1, 500, 1000)
# OC1 = OrdenCompra(1, producto1, True)
# OC1.vender(cliente1, 10, vendedor1)

# vendedor1.consultarVentas()
# print(
#     f'El total acumulado de las comisiones del vendedor {vendedor1.nombre} es igual a ${vendedor1.comision}')


# vendedor1.consultarVentas()
# print(
#     f'El total acumulado de las comisiones del vendedor {vendedor1.nombre} es igual a ${vendedor1.comision}')

# proveedor1 = Proveedor(1, 'Tia Rica', 'Tia Rica', 'Chile', True)

# print(f'El stock actual {producto1.stock}')

# proveedor1.agregarStockProducto(producto1, 100)

# print(f'El nuevo stock {producto1.stock}')