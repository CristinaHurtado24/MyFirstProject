class Clients():
    def __init__(self, name, email, password, order_status='No order'):
       self.name = name                             #Nombre del cliente
       self.email = email                           #Email del cliente
       self.__password = password                   #Metodo de pago --diccionario--
       self.order_status = order_status             #Status de la orden --Inicializado en "No order"--

    def get_password(self):
        """[getter del password]
        """
        return self.__password
    
    def show_client_info(self):
        """[Retorna la informacion del cliente]
        """
        return (f"Informacion del cliente:\nName: {self.name}\ne-mail: {self.email}\nOrder status: {self.order_status}")