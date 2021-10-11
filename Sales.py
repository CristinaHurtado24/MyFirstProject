from Clients import Clients
from Food import Food
from Drinks import Drinks
class Sales(Clients):
    def __init__(self, name, email, password, selected_products, total, payment_method, promotions='No promotions', order_status='ordered'):
        super().__init__(name, email, password, order_status='ordered')
        self.selected_products = selected_products
        self.payment_method = payment_method
        self.total = total
        self.promotions = promotions 

    def info_loyal_customer(self):
        """[Muestra la informacion de los clientes mas fieles]
        """
        return(f"\nClient's name: {self.name}\nClient's e-mail: {self.email}\nTotal: {self.total}")

    def show_invoice(self):
        """[Genera la factura o la informacion de la compra del cliente]
        """
        print(f"\nInvoice Information:\nClient's Name: {self.name}\nClient's e-mail: {self.email}\nProducts:")
        for i in range(len(self.selected_products)):
            print('\n')
            print('Product----',i+1,'-----')
            print((self.selected_products[i]).show_info_prod_client())
        print(f"\nTotal: {self.total}\nPromotions: {self.promotions}\nPayment: {self.payment_method}\nOrder Status: {self.order_status}")

   
