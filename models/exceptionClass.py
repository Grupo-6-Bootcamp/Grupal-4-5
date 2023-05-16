class sinStockBodega(Exception):
    def __init__(self, cantidad):
        self.cantidad = cantidad

    def __str__(self):
        return 'No existe stock suficiente en Bodega para reponer el producto'