from package.Menuss.Order import Order

#*voy a llamar a toda la clase order para extraer solo la lista de menu
#* la representacion de cada una ya esta definida por __str__ en las respectuvas subclases de MenuItem

class Iterator:
    def __init__(self, listord: "Order"):
        self.iterable = iter(listord.order) 

    def newiter(self, new: "Order"):
        self.iterable = iter(new.order)    
   
    def iterador(self):
        a = 0
        for i in self.iterable:
            print(i)
            a+= i.price
        return f"subtotal: {a}"
    
 


