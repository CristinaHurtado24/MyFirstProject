from Food import Food
from Drinks import Drinks
class Warehouse():
    def __init__(self, code_wh, products, wh_size,  wh_diagram):
        self.code_wh = code_wh         #Codigo del almacen
        self.products = products       #Lista de objetos producto
        self.wh_diagram = wh_diagram   #Diagrama del almacen
        self.wh_size = wh_size         #Tamaño del almacen
    
    def show_description_wh(self):
        """[Retorna la informacion del almacen]
        """
        print(f"\nWarehouse description: \nWarehouse Code: {self.code_wh}\nProducts:")
        for i in range(len(self.products)):
            self.products[i].show_product()
        print (f"\nWarehouse Size: {self.wh_size}\nWarehouse Diagram: {self.wh_diagram}\n ")
    
