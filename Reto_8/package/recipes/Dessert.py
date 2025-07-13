from package.Menuss.MenuItem import MenuItem

class Dessert(MenuItem):
    def __init__(self, name: str, price: float, gluten: bool, description: str, x: float = 0):
        self.gluten = gluten
        super().__init__(name, price, description, x)
    
    def __str__(self):
        return f"{self.name} (gluten: {self.gluten}): {self.price}, {self.description}"