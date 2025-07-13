from package.Menuss.MenuItem import MenuItem

class Beverage(MenuItem):
    def __init__(self, name: str, price: float, brand: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.brand = brand

    def __str__(self):
        return f"{self.name} - {self.brand}: {self.price}, {self.description}"
