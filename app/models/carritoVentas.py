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
        
    def eliminarProducto(self, idProductos):
     # Buscar el índice del producto con el id dado en el carrito
        indexProducto = next((index for index, item in enumerate(self.carrito) if item['producto'].idProductos == idProductos), None)

        if indexProducto is not None:
        # Eliminar el producto del carrito usando el índice encontrado
         productoEliminado = self.carrito.pop(indexProducto)
         print(f"El producto con id {idProductos} ({productoEliminado['producto'].descripcionProductos}) ha sido eliminado del carrito.")
        else:
         print(f"El producto con id {idProductos} no está en el carrito.")
         
         
    def calcularTotal(self):
      return sum(item['producto'].precioProductos * item['cantidad'] for item in self.carrito)
