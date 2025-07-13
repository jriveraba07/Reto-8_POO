from .MenuItem import MenuItem
from package.recipes.Appetizer import Appetizer
from package.recipes.Beverage import Beverage
from package.recipes.Dessert import Dessert
from package.recipes.MainCourse import MainCourse

class Order:
    def __init__(self, menu: list, tip: float = 0):
        self.menu = menu
        self.tip = tip
        self.order = []
        self.limit = 0
    
    def see_menu(self):
        n = len(self.menu)
        print("+--------------------------------------------+")
        print("|                     MENU                   |")
        print("+--------------------------------------------+")        
        for i in range(n):
            print(str(i + 1) + ".", self.menu[i])
        return f"{n}. {self.menu[n - 1]}"
    
    def add_item(self, food :"MenuItem")-> list:
        self.limit = 0
        for i in self.order:
            i.new_discount(0)
        self.order.append(food)
        return f"Se añidio {food.name} (se reiniciaron todos los descuentos)"

    def calculate_bill_amount(self):
        amount = 0
        for i in self.order:
            amount += i.calculate_total_price()
        return amount
    
    def cba_tip(self):
        return self.calculate_bill_amount() * (1 + self.tip/100)
         
    def discounts(self):
        desserts = [i for i in self.order if isinstance(i, Dessert)]
        main_coursess = [i for i in self.order if isinstance(i, MainCourse)]
        bevereages = [i for i in self.order if isinstance(i, Beverage)]
        appetizers = [i for i in self.order if isinstance(i, Appetizer)]
        if self.calculate_bill_amount() >= 80000:
            for i in self.order:
                i.new_discount(15)
            print("¡¡¡Tu cuenta es mas de 80000, 15% en la cuenta total!!!")
       
        elif len(desserts) + len(main_coursess) + len(bevereages) + len(appetizers) >= 4:
            for i in self.order:
                i.new_discount(20)
            return "¡¡¡por comprar un postre, plato fuerte, aperitivos y postre ahora tiene un 20% de descuento!!!"
        elif (len(main_coursess) + len(bevereages)) % 2 == 0 :
            for i in self.order:
                if i in main_coursess or i in bevereages:
                    i.new_discount(10)
                else:
                    pass
            return "¡¡¡por comprar cantidades pares de bebidas y de platos fuertes son un 10% mas baratos!!!"
        elif self.limit >= 0: 
            return "no puedes aplicarle descuento al descuento, bobo hpta"
        else:
            return "no hay descuentos disponibles, pobre"
