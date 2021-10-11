class Products():
    def __init__(self, code_prod, name, price, amount, prod_type, description, image ):
        self.code_prod = code_prod
        self.name = name
        self.price = price
        self.amount = amount
        self.prod_type = prod_type
        self.description = description
        self.image = image

    def show_product(self):
        """[Retorna la informacion del producto]
        """
        return (f"\nProduct Information:\nCode: {self.code_prod}\nName: {self.name}\nPrice: ${self.price}\nAmount available: {self.amount}\nType: {self.prod_type}\nDescription: {self.description}\nImage: {self.image}")

    def show_info_prod_client(self):
        """[Retorna la informacion del producto que sera mostrada al cliente]
        """
        print(f"Product's Name: {self.name}\nPrice: ${self.price}")
    
    def show_info_statistics(self):
        """[Retorna la informacion de los productos mejor vendidos]
        """
        return(f"Product's Code: {self.code_prod}\n Name: {self.name}")


        
