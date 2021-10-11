from Products import Products
from Food import Food
from Drinks import Drinks
from random import choice
from Sales import Sales
import webbrowser
import pickle


def save_data1(file_name, list_name):
    """[guarda datos en el archivo .txt]

    Args:
        file_name ([string]): [archivo .txt]
        list_name ([array]): [lista de objetos]
    """

    archive = open(file_name, 'wb+')
    pickle.dump(list_name, archive)
    archive.close()
    del archive


def read_data1(file_name):
    """[lee los datos guardados en el archivo .txt]

    Args:
        file_name ([string]): [archivo .txt]

    Returns:
        [array]: [lista de objetos]
    """
    archive = open(file_name, 'rb+')
    object_list = pickle.load(archive)
    archive.close()
    del archive
    return object_list

def ask_url(url):
    """[Pregunta al usuario si desea ver la imagen del producto]

    Args:
        url ([string]): [url del producto]
    """
    print('\nPlease enter 1 if you want to see the products image, otherwise type 2: ')
    decision = selection(3)
    if decision ==1:
        webbrowser.open(f'{url}')
    else:
        print("\nThat's all the information we have to show.")

def selection(n):
    """[Verifica si el valor ingresado por el usuario es valido o no]

    Args:
        n ([int]): [entero que determina el rango de opciones en la seleccion]

    Raises:
        Exception: [ValueError]

    Returns:
        [int]: [Numero de la seleccion]
    """
    while True:
        try:
            option = int(input('Enter the number of your selection: '))
            if option not in range(1, n):
                raise Exception
            break
        except:
            print('Please, enter a valid value.')
    return option


def code_generator(size=4):
    """[Genera aleatoriamente un codigo alfanumerico]

    Args:
        size (int, optional): [cantidad de caracteres del codigo]. Defaults to 4.
        charac ([string], optional): [Especificaciones del codigo. Por defecto se genera un codigo alfanumerico con letras en mayuscula]. Defaults to string.ascii_uppercase+string.digits.

    Returns:
        [string]: [codigo alfanumerico]
    """
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    code = "". join(choice(letters) + str(choice(digits)) for _ in range(size-2))
    return code


def verify_code_gen(products_list, warehouses):
    """[Verifica que el codigo generado aleatoriamente sea unico dentro del sistema]

    Args:
        products_list ([Array]): [Lista de productos existentes ]

    Returns:
        [String]: [El codigo del nuevo producto]
    """
    code_prod = code_generator()
    while True:
        for s in range(len(warehouses)):
            for x in range(len((warehouses[s]).products)): 
                if (((warehouses[s]).products)[x].code_prod) == code_prod:
                    code_prod = code_generator()
                else:
                    break
                break
            break
        break
    return code_prod


def new_price():
    """[Verifica que el precio del nuevo producto sea valido]

    Raises:
        Exception: [ValueError]

    Returns:
        [Int]: [Precio del producto]
    """
    while True:
        try:
            price = input('Enter the price of the new product: ')
            if (not price.isnumeric()) and (float(price) <= 0.0):
                raise Exception
            break
        except:
            print('Please, enter a valid value.')
    return float(price)


def new_quantity():
    """[Verifica que la cantidad de unidades del producto sea valida]

    Raises:
        Exception: [ValueError]

    Returns:
        [Int]: [Cantidad de unidades del producto]
    """
    while True:
        try:
            quantity = input('Enter the quantity of product units: ')
            if (not quantity.isnumeric()) and (int(quantity) <= 0):
                raise Exception
            break
        except:
            print('Please, enter a valid value.')
    return quantity


def verify_product(products_list, warehouses):
    """[Verifica que el codigo ingresado por teclado pertenezca a un producto existente]

    Args:
        products_list ([Array]): [Lista de productos]     

    Returns:
        [String]: [Codigo del producto]
    """
    code_produc = (input('Enter the code of the product: ')).upper()

    while True:
        for s in range(len(warehouses)):
            for x in range(len((warehouses[s]).products)):
                if (((warehouses[s]).products)[x].code_prod) != code_produc:
                    code_produc = (input('Please enter the code of the product: ')).upper()
            break
        break
    return code_produc


def show_prod_info(products_list, code_prod, warehouses):
    """[Muestra la informacion del producto solicitado mediante el codigo]

    Args:
        products_list ([Array]): [Lista de productos]
    """
    
    for x in range(len(warehouses)):
        for i in range(len((warehouses[x]).products)):
            if code_prod == (((warehouses[x]).products)[i]).code_prod:
                (((warehouses[x]).products)[i]).show_product()
                print('\n')
                print(f'Warehouse code: {warehouses[x].code_wh}')
                print(f'Warehouse Diagram: {warehouses[x].wh_diagram}')
                url = (((warehouses[x]).products)[i]).image
                ask_url(url)  


def percentage():
    """[Solicita el numero acorde al porcentaje de descuento deseado]

    Raises:
        Exception: [ValueError]

    Returns:
        [float]: [valor del descuento]
    """
    while True:
        try:
            per = input('Please enter the number of the percentage you want to apply: ')
            if (not per.isnumeric()) and (per <= 0):
                per = input('Please enter the number of the percentage you want to apply: ')
                raise Exception
            break
        except:
            print('Invalid value. Please try again.')
    return float(per)


def verify_code_prom(promotions_list):
    """[Verifica que el codigo de la promocion exista y pertenezca a una]

    Args:
        promotions_list ([Array]): [Lista de promociones]

    Raises:
        Exception: [ValueError]

    Returns:
        [string]: [Codigo de la promocion]
    """
    promo_code = (input("Please enter the code of the promotion you want to delete: ")).upper()
    while True:
        try:
            for x in range(len(promotions_list)):
                if not promotions_list[x].code_prom == promo_code:
                    promo_code = (input("Please enter the code of the promotion you want to delete: ")).upper()
                    raise Exception
            break
        except:
            print('Enter a valid code')
    return promo_code

def verify_promo_code(promotions_list, prom_code):
    while True:
        try:
            for i in range(len(promotions_list)):
                if promotions_list[i].code_prom == prom_code:
                    prom_code = (input("Please, enter a valid code: ")).upper()
                    raise Exception
            break
        except:
            print('Please enter a valid code')
    return prom_code

def show_promo_info(promotions_list, pr_code):
    """[Muestra la informacion de la promocion]

    Args:
        promotions_list ([Array]): [Lista de promociones]
    """

    for x in range(len(promotions_list)):
        if promotions_list[x].code_prom == pr_code:
            print(promotions_list[x].show_promotion())
            print('\n')
            break
        else:
            print("The code you entered doesn't match an existent promotion's code: ")
            break


def show_all_products(warehouses, products_list):
    """[Muestra al cliente los productos disponibles]

    Args:
        products_list ([Array]): [Lista de productos]
    """
    products_list=[]
    for x in range(len(warehouses)):
        for i in range(len(warehouses[x].products)):
            if (((warehouses[x].products)[i]).amount > 0) and (((warehouses[x].products)[i]).code_prod not in products_list):
                products_list.append(((warehouses[x].products)[i]))

    for i, prod in enumerate(products_list):
        print('\n')
        print('----', i+1, '------')
        print(prod.show_info_prod_client())

    
def show_prod_selected(products_selected):
    """[Muestra los productos seleccionados por el cliente]

    Args:
        products_selected ([array]): [lista de objetos productos]
    """

    for i, prod in enumerate(products_selected):
        print('\n')
        print('----', i+1,'------')
        print(prod.show_info_prod_client())        


def select_prod(warehouses, prod_client_list, products_list):
    """[Permite que el cliente agregue productos a su carro de compras]

    Args:
        products_list ([Array]): [Lista de productos]
        prod_client_list ([Array]): [Lista de productos del cliente que cumple la funcion de carrito de compras]

    Returns:
        [Array]: [Lista de productosd del cliente actualizada]
    """
    count = '0'
    while count == '0':

        for x in range(len(warehouses)):
            for i in range(len(warehouses[x].products)):
                if ((warehouses[x].products)[i]).amount > 0:
                    products_list.append(((warehouses[x].products)[i]))

        option = input('Enter the number that matches the product you desire: ')
        while (not option.isnumeric()) or (not int(option) >= 1):
            option = input('Invalid value. Try again: ')

        for i, prod in enumerate(products_list):  
            if i == int(option)-1:
                prod_client_list.append(prod)

        count = input('To add another product to your shopping car enter 0, if not enter another number: ')
    return prod_client_list


def delete_prod_client(prod_client_list):
    """[Permite al cliente eliminar productos de su carrito de compras]

    Args:
        prod_client_list ([Array]): [Lista de productos seleccionados por el cliente]

    Returns:
        [Array]: [Lista actualizada de los productos que el cliente desea comprar]
    """
    
    count= '0'
    while count =='0':
        for i, prod in enumerate(prod_client_list):
            print('-------', i+1, '-------')
            print(prod.show_info_prod_client())
            print('\n')

        option =input("Please enter the number of the product you want to delete of your shopping car: ")
        while (not option.isnumeric()) or (not int(option) >= 1):
            option = input('Invalid value. Try again: ')

        for i, prod in enumerate(prod_client_list):
            if i == int(option)-1:
                print('\n')
                print(prod.show_info_prod_client())
        print('Are you sure you want to delete this product?')
        decision = (input('To delete the product please enter (D), otherwise enter (N):')).upper()
        while True:
            if (not decision == 'D') and (not decision == 'N'):
                decision = (input('To delete the product please enter (D), otherwise enter (N):')).upper()
            else:
                break
        if decision == 'D':
            for i, prod in enumerate(prod_client_list):
                if i == int(option)-1:
                    prod_client_list.remove(prod)
                    print('Product deleted!\n')

            print('\nProducts in your car:\n')
            show_prod_selected(prod_client_list)
            
        else:
            print('Cancelled!\n')
            break
        
        count = input("To delete another product please enter 0, if not enter another number: ")
    return prod_client_list


def check_out(warehouses, prod_client_list, delivery_fee, promotions_list, sales_, name, email, password):   
    _total_palindromo =palindromo(prod_client_list)
    #sales_ =[]
    if len(prod_client_list)==0:
        print('You have to add products to your car to do a check-out.')
    
    elif _total_palindromo == True:
        total_ = 0
        total=0
        promo = 'No promo'
        payment_method = 'Free'
        show_prod_selected(prod_client_list)
        print('--------------\n')
        for i in range(len(prod_client_list)):
            total += prod_client_list[i].price
            total = float(redondear(total))

        iva = total*0.16
        iva = float(redondear(iva))
        total_ = total + delivery_fee + iva
        print(f"Total: ${total}")
        print(f"IVA 16%: ${iva}")
        print(f"Delivery Fee: ${delivery_fee}")
        print(f'------------------------')
        print(f'Total: ${total_}')
        print(f"Total to pay: ${_total_palindromo}")

        new_sale = Sales(name, email, password, prod_client_list, _total_palindromo, promo, payment_method)
        sales_.append(new_sale)

    else:
        total = 0
        show_prod_selected(prod_client_list)
        print('--------------\n')
        for i in range(len(prod_client_list)):
            total += prod_client_list[i].price
            total = float(redondear(total))
        
        iva = total*0.16
        iva = float(redondear(iva))
        total_1 = total + delivery_fee + iva
        total_1 = float(redondear(total_1))
        print(f"Products total: ${total}")
        print(f"IVA 16%: ${iva}")
        print(f"Delivery Fee: ${delivery_fee}")
        print(f'------------------------')
        print(f'Total to pay: ${total_1}')
        print('\n')

        if len(promotions_list)==0:
            print('Sorry, we do not have any promotions at this moment')
            discount=0.0
            promotion = 'No promo'
        else:
            discount = 0.0
            promotion = 'No promo'
            for i in range(len(promotions_list)):
                print('Promo ---', i+1, '---')
                print(promotions_list[i].show_promotion())
                print('\n')

            decision = (input('Would you like to take a promotion?\nEnter Y(yes) or N(no): ')).upper()
            while (not decision.isalpha()) and (not decision=='Y') and (not decision=='N'):
                decision = (input('Please enter Y(yes) or N(no): ')).upper()
            if decision=='Y':    
                option = input("Please enter the number of the promotion you want to take: ")
                while (not option.isnumeric()) or (not int(option) >= 1):
                    option = input('Invalid value. Try again: ')
                for i, promo in enumerate(promotions_list):
                    if i == int(option)-1:
                        promotion = promo.code_prom
                        discount = promo.discount_percent
                        discount = int(discount) /100
                    else:
                        print('The value you entered does not match any promotion')
            else:
                promotion ='No promo'
                discount =0

        total = 0
        show_prod_selected(prod_client_list)
        print('--------------\n')
        for i in range(len(prod_client_list)):
            total += prod_client_list[i].price
            total = float(redondear(total))
        
        disct = total_1*discount
        disct = float(redondear(disct))
        total_ = total + delivery_fee + iva - disct
        total_ = float(redondear(total_))
        print(f"Total: ${total}")
        print(f"IVA 16%: ${iva}")
        print(f"Delivery Fee: ${delivery_fee}")
        print(f"Promotion's discount: ${disct}")
        print(f'------------------------')
        print(f'Total to pay: ${total_}')

        payment_method = payment(total_, warehouses, prod_client_list, delivery_fee, promotions_list, name, email, password, discount, disct)
        new_sale = Sales(name, email, password, prod_client_list, total_, payment_method, promotion)
        sales_.append(new_sale)
    return sales_

def palindromo(prod_client_list):
    """[Verifica si hay algun codigo palindromo en la compra del cliente]

    Args:
        prod_client_list ([array]): [lista de objetos producto]

    Returns:
        [bool]: [retorna un booleano dependiendo del resultado del analisis]
    """

    for i in range(len(prod_client_list)):
        for x in range(0, (len(prod_client_list[i].code_prod)//2)+1):
            if ((prod_client_list[i].code_prod)[(len(prod_client_list[i].code_prod)-1)-x] == prod_client_list[i].code_prod):
                print('It must be your day!! You just got all your products for free!')
                return True
    
    return False


def show_promo_main(promotions_list):
    """[Muestra las promociones existentes en el main]

    Args:
        promotions_list ([array]): [lista de objetos promocion]
    """
    if len(promotions_list)==0:
        print('We are working on new promotions for you!! Either way you can shop without a discount\n')
    else:
        print('\nWE HAVE NEW PROMOTIONS!!\n')
        for i, promo in enumerate(promotions_list):
            print('Promo ---',i+1,'---')
            print(promo.show_promotion())
            print('\n')


def payment(total_t, warehouses, prod_client_list, delivery_fee, promotions_list, name, email, password, discount, disct):
    """[Realiza la transaccion de compra del cliente]

    Args:
        total_t ([float]): [total de la compra]
        warehouses ([array]): [lista de objetos almacen]
        prod_client_list ([array]): [lista de objetos producto]
        delivery_fee ([float]): [fee del delivery]
        promotions_list ([array]): [lista de objetos promocion]
        name ([string]): [nombre del cliente]
        email ([string]): [email del cliente]
        password ([string]): [contraseña del cliente]
        discount ([float]): [descuento por promocion]
        disct ([float]): [descuento por promocion]

    Returns:
        [dict]: [diccionario con el metodo de pago]
    """
    pay_bank = 0
    pay_cred = 0
    pay_c = 0
    payment_method={}
    while total_t >0.00:
        print(f'Total to pay: ${total_t}')
        print('\nPayment Methods:\n1. Wire Transfer\n2. Credit card\n3. Cash')
        option = selection(4)
        if option==1:                  #TRANSFERENCIA BANCARIA
            bank = input("Please enter the bank's name: ")
            while not ("".join(bank.split(" "))).isalpha():
                bank = input('Please enter a valid name: ')
            pay_bank = input('Enter the amount to pay: ')
            while (not pay_bank.isnumeric()) and (not float(pay_bank) <= total_t) and (not float(pay_bank) > 0.0):
                pay_bank = input('Enter the amount to pay: ')
            
            pay_bank = redondear(float(pay_bank))
            total_t -= float(pay_bank)
            total_t = float(redondear(total_t))
            payment_method['Wire Transfer']= float(pay_bank)

        elif option==2:               #TARJETA DE CREDITO
            card_number= input('Enter your credit card number (4 digits max): ')
            while (not card_number.isnumeric()) or (not len(card_number)<=4):
                card_number= input('Enter your credit card number (4 digits max): ')
            
            pay_cred = input('Enter the amount to pay: ')
            while (not pay_cred.isnumeric()) and (not float(pay_cred) <= total_t) and (not float(pay_cred) > 0.0):
                pay_cred = input('Enter the amount to pay: ')

            pay_cred = redondear(float(pay_cred))
            total_t -= float(pay_cred)
            total_t = float(redondear(total_t))
            payment_method['Credit Card']= float(pay_cred)

        else:                          #EFECTIVO
            pay_c = input('Enter the amount to pay: ')
            while (not pay_c.isnumeric()) and (not float(pay_c)<= total_t) and (not float(pay_c) > 0.0):
                pay_c = input('Enter the amount to pay: ')
            
            pay_c = redondear(float(pay_c))
            total_t -= float(pay_c)
            total_t = float(redondear(total_t))
            payment_method['Cash']= float(pay_c)
    
    print('\nResume:\n')
    total = 0
    show_prod_selected(prod_client_list)
    print('--------------\n')
    for i in range(len(prod_client_list)):
        total += prod_client_list[i].price
        total = float(redondear(total))

    iva = total*0.16
    iva = float(redondear(iva))
    disct = total*discount
    disct = float(redondear(disct))
    total_ = total + delivery_fee + iva - disct
    total_ = float(redondear(total_))
    print(f"Total: ${total}")
    print(f"IVA 16%: ${iva}")
    print(f"Delivery Fee: ${delivery_fee}")
    print(f"Promotion's discount: ${disct}")
    print(f'------------------------')
    print(f'Total to pay: ${total_}')
    print(f'------------------------')
    if float(pay_c) >0.0:
        print(f"Cash: ${pay_c}")
    elif float(pay_cred) >0.0:
        print(f"Credit: ${pay_cred}")
    elif float(pay_bank) >0.0:
        print(f"Wire Bank: ${pay_bank}")
    print(f"------------------------")
    print(f'Total deb: ${total_t}')

    
    act_prod_quantity(prod_client_list, warehouses)
    
    return payment_method

def locate_pro_diag(new_product, warehouses):
    """[Permite ubicar un nuevo producto dentro de un almacen]

    Args:
        new_product ([object]): [Objeto del nuevo producto]
        warehouses ([array]): [Lista de almacenes]
    """
    for i, warehouse in enumerate(warehouses):
        print('\n')
        print('Warehouse-----',i+1,'--------')
        print(f'Warehouse Code: {warehouse.code_wh}')
        print(f'Warehouse Diagram: {warehouse.wh_diagram}')
    
    option = input('\nPlease enter the number that matches the warehouse were you want to locate the new product: ')
    while (not option.isnumeric()) or (int(option) not in range(1,(len(warehouses)+1))):
        option = input('Please enter the number that matches the warehouse were you want to locate the new product: ')
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i, warehouse in enumerate(warehouses):
        if (int(option)-1) == i:
            print('\n')
            print(f'Warehouse Code: {warehouse.code_wh}')
            print(f'Warehouse Diagram: {warehouse.wh_diagram}')

            corridor = input('\nPlease enter the number of the corridor: ')
            while (not corridor.isnumeric()) or (int(corridor) not in range(1,(((warehouse.wh_size)[0])+1))):
                corridor = input('Please enter a valid value: ')
            
            print('\n')
            for x in range(1, (((warehouse.wh_size)[0])+1)):
                if int(corridor) == x: 
                    space = (input('\nPlease enter the letter of the space: ')).upper()
                    while (not space.isalpha()) and (not space in letters):
                        space = (input('Please enter a valid value: ')).upper()
                    for s in range(0, (((warehouse.wh_size)[1]))):
                        if (space == letters[s]):
                            if (warehouse.wh_diagram[x][letters[s]][0]) == 'Available':
                                warehouse.wh_diagram[x][letters[s]] =['Busy', (new_product.code_prod)]
                                (warehouse.products).append(new_product)
                                warehouses = save_data1('info_warehouses.txt', warehouses)
                                print('Product added')
                                return warehouses
                            else:
                                print('You cannot place your new product here, this space is Busy.')
                                del(new_product)
                                print('The product was deleted, please try again')
                                break
                            break
                            
                        
def change_location(warehouses, product):  
    """[Cambiar ubicacion del producto entre almacenes]

    Args:
        warehouses ([array]): [Lista de objetos almacen]
        product ([object]): [objeto producto que se desea reubicar]
    """
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']                          
    
    for i, warehouse in enumerate(warehouses):
        print('\n')
        print('Warehouse-----', i+1, '--------')
        print(f'Warehouse Code: {warehouse.code_wh}')
        print(f'Warehouse Diagram: {warehouse.wh_diagram}')
    
    option = input('\nPlease enter the number that matches the warehouse were you want to locate the product: ')
    while (not option.isnumeric()) or (int(option) not in range(1, (len(warehouses)+1))):
        option = input('Please enter the number that matches the warehouse were you want to locate the product: ')
    
    warehouse_selected =0
    for i in range(len(warehouses)):
        print(warehouses[i])
        if int(option)-1 ==i:
            print(f'Warehouse Code: {warehouses[i].code_wh}')
            print(f'Warehouse Diagram: {warehouses[i].wh_diagram}')   #Numero de espacios
            warehouse_selected = warehouses[i]
    
    corridor = input('\nPlease enter the number of the corridor: ')
    while (not corridor.isnumeric()) or (int(corridor) not in range(1, ((warehouse_selected.wh_size)[0])+1)):
        corridor = input('Please enter a valid value: ')

    print('\n')
    for x in range(1, ((warehouse_selected.wh_size)[0])+1):           #Reubicar
        if (int(corridor)) == x:
            space = (input('\nPlease enter the letter of the space: ')).upper()
            while (not space.isalpha()) and (not space in letters):
                space = (input('Please enter a valid value: ')).upper()
            for s in range(0, ((warehouse_selected.wh_size)[1])):
                if (space == letters[s]):
                    if (warehouse_selected.wh_diagram[x][letters[s]][0]) == 'Available':
                        warehouse_selected.wh_diagram[x][letters[s]] = ['Busy', product.code_prod]
                        (warehouse_selected.products).append(product)
                        return True
                    else:
                        print('You cannot place your product here, this space is Busy.')
                        return False
    
def get_prod_location(warehouses, code_prod):
    """[Localiza el producto que se desea reubicar]

    Args:
        warehouses ([array]): [Lista de objetos almacen]
        code_prod ([string]): [Codigo del producto que se desea reubicar]
    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    inicial_list =0
    product =0
    inicial_diagram = 0
    found = False
    for x in range(len(warehouses)):  # lista objetos almacen
        for u in range(len(warehouses[x].products)):  #Lista de objetos productos del almacen
            if code_prod == ((warehouses[x].products)[u].code_prod):
                product = ((warehouses[x].products)[u])
                print('\nThe product you entered is located in this warehouse:\n')
                print(warehouses[x].wh_diagram)
                inicial_diagram = warehouses[x].wh_diagram
                inicial_list = (warehouses[x].products)
                print('\n')
                print("Do you want to keep the product in this warehouse?")
                decision = (input('Type Y(yes) or N(no): ')).upper()
                while (not decision.isalpha()) and (not decision == 'Y') and (not decision == 'N'):
                    decision = (input('Invalid value. Type Y(yes) or N(no): ')).upper()

                if decision == 'Y':           #DENTRO DEL MISMO ALMACEN
                    warehouses[x] = change_location_same_wh(warehouses, product, warehouses[x])

                else:                         #CAMBIAR DE ALMACEN
                    if change_location(warehouses, product) == True:    
                        for s in range(len((warehouses[x]).wh_diagram)):         #Num pasillo
                            for w in range(0, ((warehouses[x]).wh_size)[1]):     # Num espacio
                                if ((inicial_diagram)[s+1][letters[w]][1] == (product.code_prod)):
                                    ((inicial_diagram))[s+1][letters[w]] = ['Available', 'No product']
                                    inicial_list.remove(product)
                                    print("\nProduct's location changed!!")
                                    break

                            
                        
                    else:
                        break
                found = True
                break
        if found:
            break
            
                    


    

def change_location_same_wh(warehouses, product, wh_located):
    """[Reubica el producto deseado dentro del almacen en el que estaba originalmente]

    Args:
        warehouses ([array]): [Lista de objetos almacen]
        product ([object]): [Objeto producto que se desea reubicar]
        wh_located ([object]): [Objeto almacen en el que se encuentra el producto]

    Returns:
        [type]: [description]
    """

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for a in range(1, ((wh_located.wh_size)[0])+1):       
        for b in range(0, ((wh_located.wh_size)[1])):
            if (wh_located.wh_diagram[a][letters[b]][0]) == 'Available' or (wh_located.wh_diagram[a][letters[b]][0]) == 'Busy':
                if (wh_located.wh_diagram[a][letters[b]][1]) == product.code_prod:
                    (wh_located.wh_diagram[a][letters[b]]) = ['Available', 'No Product']
                    print(wh_located.wh_diagram)


    corridor = input('\nPlease enter the number of the corridor: ')
    while (not corridor.isnumeric()) or (int(corridor) not in range(1, ((wh_located.wh_size)[0])+1)):
        corridor = input('Please enter a valid value: ')

    print('\n')
    for z in range(1, ((wh_located.wh_size)[0])+1):           #Reubicar dentro del mismo almacen
        if (int(corridor)-1) == z:
            space = (input('\nPlease enter the letter of the space: ')).upper()
            while (not space.isalpha()) and (not space in letters):
                space = (input('Please enter a valid value: ')).upper()
            for d in range(0, ((wh_located.wh_size)[1])):
                if (space == letters[d]):
                    if (wh_located.wh_diagram[z+1][letters[d]][0]) == 'Available':
                        wh_located.wh_diagram[z+1][letters[d]] = ['Busy', product.code_prod]
                        return wh_located
                    else:
                        print('You cannot place your product here, this space is Busy.')
                        return False


def redondear(n):
    """[Redondea el monto a pagar con 3 decimales]

    Args:
        n ([int]): [Monto a pagar]

    Returns:
        [int]: [Monto redondeado]
    """
    return ("{:.3f}".format(n))


def act_prod_quantity(prod_client_list, warehouses):
    """[Actualiza el stock del almacen luego de cada compra]

    Args:
        prod_client_list ([array]): [Lista de productos seleccionados por el cliente]
        warehouses ([array]): [lista de objetos almacen]
    """
    
    for x in range(len(prod_client_list)):
        prod_client_list[x].amount -= 1
    
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
               'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    

    codes = []
    for x in range(len(warehouses)):
        for i in range(len(warehouses[x].products)):
            if ((warehouses[x].products)[i].amount == 0) or ((warehouses[x].products)[i].amount < 0):
                codes.append(((warehouses[x].products)[i]))

    for z in range(len(warehouses)):       
        for s in range(((warehouses[z].wh_size)[0])):
            for t in range(((warehouses[z].wh_size)[1])):
                for a in range(len(codes)):
                    if (warehouses[z].wh_diagram)[s+1][letters[t]][1] == codes[a].code_prod:
                        (warehouses[z].wh_diagram)[s+1][letters[t]] = ['Available','No product']
    
    if len(codes)!=0:
        for a in range(len(codes)):
            product = codes[a]
            for b in range(len(warehouses)):
                for c in range(len(warehouses[b].products)):
                    if ((warehouses[b].products)[c]).code_prod == product.code_prod:
                        del(((warehouses[b].products)[c]))
                        break
                    
                
            break


