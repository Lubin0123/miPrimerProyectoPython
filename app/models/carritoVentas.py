from app.models.Productos import Productos

class CarritoVentas:
    def __init__(self):
        self.carrito = [] # en este caso se iniicializa carrito como una lista vacia#


    def agregarProducto(self, idProductos, cantidadProductos):
        producto = Productos.query.get(idProductos)
        if producto:
            item = {'producto': producto, 'cantidad': cantidadProductos}
            self.carrito.append(item) # con el metodo append se agreaga los datos que contien el diccionario a la base de datos#

    def calcularTotal(self):
        return sum(item['producto'].precioproductos * item['cantidadProductos'] for item in self.carrito)
    
    def tamanoD(self):   
        return len(self.carrito)

    def getItems(self):
        return self.carrito
    
    def vaciarcarrito(self):
        self.carrito = []
