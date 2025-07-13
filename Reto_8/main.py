from package.Menuss.Order import Order 
from package.recipes.Appetizer import Appetizer
from package.recipes.Beverage import Beverage
from package.recipes.Dessert import Dessert
from package.recipes.MainCourse import MainCourse
from package.Iterator import Iterator

if __name__ == '__main__':         
    milhoja = Dessert("milhoja", 7500, True, "Postre con mil hojas")
    pollo_asado = MainCourse("pollito asado", 40000, "pollo","Un pollo asado de dudosa procedencia")
    bistec = MainCourse("bistec", 25000, "carne", "Hecho de las vacas de genetica en la nacional")
    natilla = Dessert("natilla", 5000, True, "Delicioso postre colombiano con leche de bufalo")
    changua = Appetizer("changua", 9500, 500,"leche con huevo (¿Quien creyo que era buena idea esto?)")
    cerveza_1 = Beverage("cerveza", 3500, "poker", "Cerveza que toma el rolo promedio")
    aguardiente = Beverage("aguardiente 1/2", 16000, "nectar", "Agua que pica pero rico")
    chunchullo = Appetizer("chunchullo", 12000, 200, "No preguntes de donde viene, solo disfrutalo")
    mojarra = MainCourse("mojarra", 40000, "pescado","OJO CON LAS ESPINAS")
    limonada = Beverage("limonada de coco", 3500, "frutiño", "Limonada hecha con agua de la llave")

    menu = [milhoja, pollo_asado, bistec, natilla, changua, cerveza_1, aguardiente, chunchullo, mojarra, limonada]
    cliente = Order(menu, tip = 0)
    cliente.see_menu()
    
    print("----------------------------------------------------------------------------------------")
    print("")
    print(cliente.add_item(pollo_asado))
    print(cliente.add_item(bistec))
    
    print("")
    print("lo que has pedido: ")
    print("")
    #* Lo nuevo

    Iter = Iterator(cliente)
    Iter.iterador()
    print(cliente.discounts())
    print("")

    print(cliente.add_item(mojarra))
    print(cliente.add_item(milhoja))
    print(cliente.add_item(changua))

    print("")
    Iter.newiter(cliente) #* actualizo ya que hubo cambios
    Iter.iterador()
    print("")
    cliente.calculate_bill_amount()
    cliente.discounts()
    a = float(input(f"cuanto porcentaje de la cuenta quieres agregar (cuenta actual con descuentos: {cliente.calculate_bill_amount()}): "))
    cliente.tip = a
    print(f"Total a pagar: {cliente.cba_tip()}, cuenta de {cliente.calculate_bill_amount()} con propina de: {cliente.tip}%" )


