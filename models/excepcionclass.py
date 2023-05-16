# Además se solicita crear una Excepción personalizada (Excepción definida por el usuario), la cual nos
# permite realizar una acción al momento de que no exista stock de productos en la clase Producto,
# Sucursal y Bodega.
# La clase de Excepción deberá estar en un archivo externo y se deberá importar al proyecto principal.

class SinStock(Exception):
    def __init__(self, mensaje):
        super().__init__(self.mensaje)
        self.mensaje = mensaje
    
