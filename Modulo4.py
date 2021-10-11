from Sales import Sales
from Functions import selection
from Functions import redondear
#import numpy as np
#import matplotlib
#matplotlip.use('agg')
#import matplotlib.pyplot as plt

def customer_spend(sales_):
    """[Calcula el promedio de gasto de los clientes]

    Args:
        sales ([array]): [Lista de objetos en donde estan las ventas registradas]
    """
    
    if len(sales_)==0:
        print('sorry, there are no sales registered at this moment')
    
    else:
        total=0
        for x in range(len(sales_)):
            total += sales_[x].total
        average = (float(total) / len(sales_))
        average = float(redondear(average))
        print(f"\nThe average customer Spend is: ${average}")
        print('\n')


def customer_promotions(sales_):
    """[Porcentaje de clientes que usa codigos promocionales]

    Args:
        sales ([Array]): [Lista de objetos en donde estan las ventas registradas]
    """

    if len(sales_)==0:
        print('sorry, there are no sales registered at this moment')
    
    else:
        x=0
        for x in range(len(sales_)):
            if (not sales_[x].promotions == 'No promo') and (not sales_[x].promotions == 0):
                x+=1
        
        average = (x / len(sales_)) *100
        average = float(redondear(average))
        print(f"\nThe average of customers that uses promotions is: {average}%")
       
def loyal_customer(sales_):
    """[Imprime el top 3 de los clientes mas fieles]

    Args:
        sales ([array]): [Lista de objetos en donde estan las ventas registradas]
    """
    if len(sales_)==0:
        print('sorry, there are no sales registered at this moment')

    else:
        ordered = sorted(sales_, key=lambda sale : sale.total, reverse=True) 
        if len(ordered) ==1:
            print('\nFirst place:', ordered[0].info_loyal_customer())
        
        elif len(ordered) ==2:
            print('\nFirst place:', ordered[0].info_loyal_customer())
            print('\nSecond place: ', ordered[1].info_loyal_customer())
    
        else:
            print('\nFirst place:', ordered[0].info_loyal_customer())
            print('\nSecond place: ', ordered[1].info_loyal_customer())
            print('\nThird place: ', ordered[2].info_loyal_customer())
            

def best_sold(sales_):
    if len(sales_) == 0:
        print('sorry, there are no sales registered at this moment')
    
    else:
        total_products = []
        counted_products ={}
        for i in range(len(sales_)):
            for x in range(len(sales_[i].selected_products)):
                total_products.append((sales_[i].selected_products)[x])
        
        ordered = sorted(total_products, key=lambda y: y.code_prod)
        for i in range(len(ordered)):
            print(ordered[i].code_prod)

        z=0
        i=1
        count =0
        while z< len(ordered):
            prod = {}
            while i < len(ordered):
                if ordered[z].code_prod != ordered[i].code_prod:
                    i+=1
                else:
                    count += 1
                    del(ordered[i])
                    prod['product'] = total_products[z]
                    prod['sold'] = count
                    counted_products = prod

        ordered_1= sorted(counted_products, key=lambda t: t['sold'], reverse=True)
        if len(ordered_1)==1:
            print('\nFirst best sold product: ', ordered[0][0].show_info_statistics())
        elif len(ordered_1)==2:
            print('\nFirst best sold product: ', ordered[0][0].show_info_statistics())
            print('\nSecond best sold product: ', ordered[1][0].show_info_statistics())
        elif len(ordered_1)>3:
            print('\nFirst best sold product: ', ordered[0][0].show_info_statistics())
            print('\nSecond best sold product: ', ordered[1][0].show_info_statistics())
            print('\nThird best sold product: ', ordered[2][0].show_info_statistics())


def free_sales(sales_):
    """[Calcula la cantidad de ventas gratis]

    Args:
        sales_ ([array]): [lista de objetos sales]
    """
    if len(sales_) == 0:
        print('sorry, there are no sales registered at this moment')

    else:
        y = 0
        for x in range(len(sales_)):
            if sales_[x].total ==0:
                y+=1
        
        print(f'Total sales: {len(sales_)}')
        print(f'Total of free sales: {y}')
        

def modulo4(sales_):
    """[main del modulo 4]

    Args:
        sales_ ([array]): [lista de objetos sales]
    """
    print('Hello! this is the statistics module!\n')
    while True:
        print('\nWhat would you like to do?')
        print('\n1. Average Customer Spend\n2. Average Customer-Promotions\n3. Most Loyal Customers\n4. Best Sold Products\n5. Free Sales\n6. Exit ')
        option =selection(7)
        if option==1:                  #PROMEDIO DE GASTO POR CLIENTE
            customer_spend(sales_)
        elif option==2:                #PROMEDIO DE CLIENTES QUE UTILIZAN PROMOCIONES
            customer_promotions(sales_)
        elif option==3:                #TOP 3 CLIENTES MAS FIELES
            loyal_customer(sales_)
        elif option==4:                #TOP 3 PRODUCTOS MEJORES VENDIDOS
            best_sold(sales_)
        elif option==5:                #PROMEDIO DE VENTAS GRATIS
            free_sales(sales_)
        else:
            break
