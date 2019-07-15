#---------------INCOMPLETE------------------
def pizza_point(customers):
    for customer in customers:
        total = 0
        min_price = 20
        min_orders = 5
        eligible = []
        for order in customers[customer]:
            size = customers[customer]
            total += order 
            if total >= min_price and size >= min_orders:
                eligible.append(customer)
    print('Eligible customers : ', eligible)

customers = {'roma' : [2,4,5,6,7,3,57,8],
            'leej' : [6,4,7,4,2,4,7],
            'lyma' : [5,4,2,1,345,67]}
pizza_point(customers)
