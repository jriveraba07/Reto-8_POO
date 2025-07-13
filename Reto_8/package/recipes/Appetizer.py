from package.Menuss.MenuItem import MenuItem

class Appetizer(MenuItem):
    def __init__(self, name: str, price: float, cantidad: float, description: str, x: float = 0):
        self.cantidad = cantidad
        super().__init__(name, price, description, x)   

    def __str__(self):
        return f"{self.name} (cantidad: {self.cantidad} gr): {self.price}, {self.description}"