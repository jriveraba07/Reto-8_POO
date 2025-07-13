from package.Menuss.MenuItem import MenuItem

class MainCourse(MenuItem):
    def __init__(self, name: str, price: float, type: str, description: str, x: float = 0):
        super().__init__(name, price, description, x)
        self.type = type
    
    def __str__(self):
        return f"{self.name} ({self.type}): {self.price}, {self.description}"  