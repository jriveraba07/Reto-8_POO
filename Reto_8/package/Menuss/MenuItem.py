
class MenuItem:
    def __init__(self,name: str, price: float, description: str = "", x: float = 0) :
        self.name = name
        self.price = price 
        self.discount = x
        self.description = description
    
    def calculate_total_price(self)-> float:
        a = self.price * (1 - self.discount/100)
        self.x = 0 
        return a
    
    def new_discount(self, tacaño)->float:
        if tacaño == 0:
            self.discount = 0
        else:
            self.discount += tacaño