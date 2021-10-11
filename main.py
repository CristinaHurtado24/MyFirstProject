"""[MAIN PAGE]
    """
from Modulo1 import modulo1
from Modulo2 import modulo2_productos
from Modulo2 import modulo2_promociones
from Modulo2 import modulo2_promociones1
from Modulo2 import change_order_status
from Modulo2 import delivery_fee
from Modulo2 import delivery_fee1
from Modulo3 import modulo3
from Modulo3 import modulo3_1
from Modulo4 import modulo4 
from Functions import selection
from Sales import Sales
from Warehouse import Warehouse
from Modulo2 import save_data
from Modulo2 import read_data

def main_page_reset():           ##PROGRAMA CON LA INFORMACION BASICA BRINDADA POR API
    """[Main page del programa solo con la info de la API]
    """
    clients_list=[]
    codes_wh = []
    codes_products_list = []
    products_list=[]
    promotions_list =[]
    sales_=[]
    warehouses = []
    deli_fee=0
    print("***WELCOME TO SAMAN'S DELIVERY MAIN PAGE***\n")
    while True:
        print("Modules:\n1. Warehouse Management Module\n2. Products Management Module\n3. Sales Module\n4. Statistics Module\n5. Exit\n")
        option = selection(6)

        modulo1(warehouses, codes_products_list, codes_wh)
        warehouses = read_data('info_warehouses.txt')

        if option==1:                   #MODULO DE GESTION DEL ALMACEN
            print('We only have two warehouses:\nType 1 if you want to see the Warehouse a001 info.\nType 2 if you want to see Warehouse a002 info.')
            option = selection(3)
            warehouses = read_data('info_warehouses.txt')
            if option ==1:
                warehouses[0].show_description_wh()
            elif option==2:
                warehouses[1].show_description_wh()
        
        elif option==2:                 #MODULO DE GESTION DE PRODUCTOS
            while True: 
                print('\nWhat would you like to do now?\n1. Manage Products\n2. Manage Promotions\n3. Manage Delivery Fee\n4. Manage orders status\n5. Exit\n')
                option = selection(6)
                warehouses = read_data('info_warehouses.txt')
                if option==1:            #GESTION DE PRODUCTOS
                    modulo2_productos(products_list, warehouses)

                elif option==2:          #GESTION DE PROMOCIONES
                    promotions_list= modulo2_promociones1(promotions_list)

                elif option==3:          #GESTION DE DELIVERY FEE
                    deli_fee = delivery_fee1(deli_fee)
                
                elif option==4:          #GESTION DE LOS STATUS DE LAS ORDENES
                    change_order_status(sales_)
                else:
                    break
        
        elif option==3:                  #MODULO DE VENTAS
            sales_ = modulo3_1(clients_list, promotions_list, deli_fee, sales_, warehouses)
        
        elif option==4:                  #MODULO DE ESTADISTICAS 
            modulo4(sales_)
        
        else:
            print('***GOOD BYE!! WE HOPE YOU COME BACK SOON!***')
            break

def actual_main_page():        ##INFORMACION GUARDADA EN EL TXT POR INGRESOS ANTERIORES
    """[Main page del programa con informacion guardada en txt de ingresos anteriores]
    """
    clients_list = []
    codes_wh = []
    codes_products_list = []
    products_list = []
    promotions_list = []
    sales_ = []
    warehouses = []
    deli_fee = 0
    print("***WELCOME TO SAMAN'S DELIVERY MAIN PAGE***\n")
    while True:
        print("Modules:\n1. Warehouse Management Module\n2. Products Management Module\n3. Sales Module\n4. Statistics Module\n5. Exit\n")
        option = selection(6)

        warehouses = read_data('info_warehouses.txt')

        if option == 1:  # MODULO DE GESTION DEL ALMACEN
            print('We only have two warehouses:\nType 1 if you want to see the Warehouse a001 info.\nType 2 if you want to see Warehouse a002 info.')
            option = selection(3)
            warehouses = read_data('info_warehouses.txt')
            if option == 1:
                warehouses[0].show_description_wh()
            elif option == 2:
                warehouses[1].show_description_wh()

        elif option == 2:  # MODULO DE GESTION DE PRODUCTOS
            while True:
                print('\nWhat would you like to do now?\n1. Manage Products\n2. Manage Promotions\n3. Manage Delivery Fee\n4. Manage orders status\n5. Exit\n')
                option = selection(6)
                if option == 1:  # GESTION DE PRODUCTOS
                    warehouses = read_data('info_warehouses.txt')
                    modulo2_productos(products_list, warehouses)

                elif option == 2:  # GESTION DE PROMOCIONES
                    promotions_list = modulo2_promociones(promotions_list)

                elif option == 3:  # GESTION DE DELIVERY FEE
                    deli_fee = delivery_fee(deli_fee)

                elif option == 4:  # GESTION DE LOS STATUS DE LAS ORDENES
                    sales_= read_data('sales.txt')
                    change_order_status(sales_)
                else:
                    break

        elif option == 3:  # MODULO DE VENTAS
            sales_ = modulo3(clients_list, promotions_list, deli_fee, sales_, warehouses)

        elif option == 4:  # MODULO DE ESTADISTICAS
            sales_ = read_data('sales.txt')
            modulo4(sales_)

        else:
            print('***GOOD BYE!! WE HOPE YOU COME BACK SOON!***')
            break

def main():
    """[Main del programa]
    """
    print('Would you like to update the data base according to the information given by API? Type 1 if so, or 2 otherwise:')
    selec = selection(3)

    if selec ==1:
        main_page_reset()

    else:
        actual_main_page()

if __name__ == '__main__':
    main()
    
