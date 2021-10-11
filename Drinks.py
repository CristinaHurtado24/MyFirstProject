class Drinks(Products):
    def __init__(self, code_prod, name, price, amount, prod_type, alcoholic, description, image):
        self.alcoholic = alcoholic   #Si la bebida es alcoholica o no
        super().__init__(code_prod, name, price, amount, prod_type, description, image)

    def show_product(self):
        """[Imprime la informacion del producto]
        """
        print(f'\nProduct Information:\nCode: {self.code_prod}\nName: {self.name}\nPrice: ${self.price}\nAmount Available: {self.amount}\nType: Drink\nAlcoholic: {self.alcoholic}\nDescription: {self.description}\nImage: {self.image}')

    def show_info_prod_client(self):
        """[Imprime la informacion del producto que sera mostrada al cliente]
        """
        return(f"Product's Name: {self.name}\nPrice: ${self.price}")
    
    def show_info_statistics(self):
        """[Retorna la informacion de los productos mejor vendidos]
        """
        return(f"Product's Code: {self.code_prod}\n Name: {self.name}")
    