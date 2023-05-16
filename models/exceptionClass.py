class sinStockBodega(Exception):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return 'No existe stock suficiente en Bodega para reponer el producto'

class cantMaxCarrito(Exception):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return 'No puede llevar más de 10 productos a la vez.'

class numMinimoCompras(Exception):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return 'Debe haber al menos una compra para calcular el promedio.'