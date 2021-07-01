from django.db import connection

def return_data(status, status_code, data, msg, count='0'):
    return_data = {
        'status': status,
        'status_code': status_code,
        'data': data,
        'count' : count,
        'message': msg,
    }
    return return_data

def dictfetchall(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]

def dictfetchone(cursor = ''):
    # "Returns all rows from a cursor as a dict"
    desc = cursor.description
    return dict(zip([col[0] for col in desc], cursor.fetchone()))

################################# ADMIN's functions ###############################################

def checkIngredientExists(ingredient):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT ingredient_name FROM ingredient_table; ''')
        ingredients = dictfetchall(cursor)
        for ingredient_list in ingredients:
            if ingredient == ingredient_list['ingredient_name']:
                return True
    return False

def insertItem(ingredient, quantity):
    with connection.cursor() as cursor:
        response = cursor.execute('''INSERT INTO ingredient_table(ingredient_name, quantity) VALUES (%s, %s);''', [ingredient, quantity])
    if response:
        return True
    else:
        return False

def checkIngredients(ingredient):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT ingredient_name FROM ingredient_table; ''')
        ingredients = dictfetchall(cursor)
        for i in ingredients:
            if ingredient == i['ingredient_name']:
                return True
    return False

def createItem(item_name, item_quantity, ingredient_list, ingredient_list_array, quantity, cost_price, selling_price):
    with connection.cursor() as cursor:
        ingredient_id_array = []
        for ingredient in ingredient_list_array:
            cursor.execute(''' SELECT ingredient_id FROM ingredient_table WHERE ingredient_name=%s ''', [ingredient])
            response = dictfetchone(cursor)
            if response:
                ingredient_id_array.append(response['ingredient_id'])
        ingredient_id_array = str(ingredient_id_array).replace('[','')
        ingredient_id_array = str(ingredient_id_array).replace(']','')
        print(item_quantity)
        response = cursor.execute('''INSERT INTO bakery_items(item_name, ingredients, ingredient_ids, ingredient_quantity, item_quantity, cost_price, selling_price) VALUES (%s, %s, %s, %s, %s, %s, %s);''', [item_name, ingredient_list, ingredient_id_array, quantity, str(item_quantity), cost_price, selling_price])
    if response:
        return True
    else:
        return False

def checkItem(item_name):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT item_name FROM bakery_items WHERE item_name=%s;''', [item_name])
        if cursor.rowcount > 0:
            items = dictfetchone(cursor)
            if item_name == items['item_name']:
                return True
    return False

def getItemDetails(item_name):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT * FROM bakery_items WHERE item_name = %s;''', [item_name])
        response = dictfetchone(cursor)
        if response:
            return response
    return False

def updateItemName(old_item_name, new_item_name):
    with connection.cursor() as cursor:
        response = cursor.execute(''' UPDATE bakery_items SET item_name=%s WHERE item_name=%s; ''', [new_item_name, old_item_name])
    if response:
        return True
    else:
        return False

def updateItemDetails(item_name, quantity, cost_price, selling_price):
    with connection.cursor() as cursor:
        if quantity and cost_price and selling_price:
            response = cursor.execute(''' UPDATE bakery_items SET item_quantity=%s, cost_price=%s, selling_price=%s WHERE item_name=%s;''', [quantity, cost_price, selling_price, item_name])
        elif quantity and cost_price:
            response = cursor.execute(''' UPDATE bakery_items SET item_quantity=%s, cost_price=%s WHERE item_name=%s;''', [quantity, cost_price, item_name])            
        elif quantity and selling_price:
            response = cursor.execute(''' UPDATE bakery_items SET item_quantity=%s, selling_price=%s WHERE item_name=%s;''', [quantity, selling_price, item_name])
        elif cost_price and selling_price:
            response = cursor.execute(''' UPDATE bakery_items SET cost_price=%s, selling_price=%s WHERE item_name=%s;''', [cost_price, selling_price, item_name])
        elif cost_price:
            response = cursor.execute(''' UPDATE bakery_items SET cost_price=%s WHERE item_name=%s;''', [cost_price, item_name])
        elif selling_price:
            response = cursor.execute(''' UPDATE bakery_items SET selling_price=%s WHERE item_name=%s;''', [selling_price, item_name])
        elif quantity:
            response = cursor.execute(''' UPDATE bakery_items SET item_quantity=%s WHERE item_name=%s;''', [quantity, item_name])

    if response:
        return True
    else:
        return False

def deleteItemDetails(item_name, quantity, cost_price, selling_price):
    with connection.cursor() as cursor:
        if item_name:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE item_name=%s ''', [item_name])
        elif quantity and cost_price:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE item_quantity=%s AND cost_price=%s ''', [quantity, cost_price])
        elif quantity and selling_price:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE item_quantity=%s AND selling_price=%s ''', [quantity, selling_price])
        elif cost_price and selling_price:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE cost_price=%s AND selling_price=%s ''', [cost_price, selling_price])
        elif cost_price:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE cost_price=%s ''', [cost_price])
        elif selling_price:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE selling_price=%s ''', [selling_price])
        elif quantity:
            response = cursor.execute(''' DELETE FROM bakery_items WHERE item_quantity=%s ''', [quantity])

    if response:
        return True
    else:
        return False

def getAllItemDetails():
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM bakery_items; ''')
        if cursor.rowcount > 0:
            response = dictfetchall(cursor)
            if response:
                return response
        return False

def checkIngredient(ingredient):
    with connection.cursor() as cursor:
        cursor.execute('''SELECT ingredient_name FROM ingredient_table WHERE ingredient_name=%s;''', [ingredient])
        if cursor.rowcount > 0:
            ingredients = dictfetchone(cursor)
            if ingredient == ingredients['ingredient_name']:
                return True
    return False

def updateIngredientName(old_ingredient_name, new_ingredient_name):
    with connection.cursor() as cursor:
        response = cursor.execute(''' UPDATE ingredient_table SET ingredient_name=%s WHERE ingredient_name=%s; ''', [new_ingredient_name, old_ingredient_name])
    if response:
        return True
    else:
        return False

def updateIngredientDetails(ingredient_name ,quantity):
    with connection.cursor() as cursor:
        response = cursor.execute(''' UPDATE ingredient_table SET quantity=%s WHERE ingredient_name=%s;''', [quantity, ingredient_name])
    if response:
        return True
    else:
        return False

def deleteIngredientDetails(ingredient_name, quantity):
    with connection.cursor() as cursor:
        if ingredient_name:
            response = cursor.execute(''' DELETE FROM ingredient_table WHERE ingredient_name=%s ''', [ingredient_name])
        elif quantity:
            response = cursor.execute(''' DELETE FROM ingredient_table WHERE quantity=%s ''', [quantity])
    if response:
        return True
    else:
        return False

def getAllIngredientDetails():
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM ingredient_table; ''')
        if cursor.rowcount > 0:
            response = dictfetchall(cursor)
            if response:
                return response
        return False

def findPopularProducts():
    popular_item_list = [] 
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT DISTINCT order_items FROM bakery_orders ''')
        if cursor.rowcount > 0:
            response = dictfetchall(cursor)
            print(response)
            if response:
                for i in response:
                    for j, k in i.items():
                        if ',' not in k:
                            popular_item_list.append(k.strip())
                return popular_item_list
        return False

def findPopularityOfItem(item):
    statemet = "SELECT * FROM `bakery_orders` WHERE order_items REGEXP '" + item.strip() + " *';"
    with connection.cursor() as cursor:
        cursor.execute(statemet)
        if cursor.rowcount > 0:
            response = dictfetchall(cursor)
            if response:
                return len(response)
    return False

def updateDiscount(item_name, discount_value):
    with connection.cursor() as cursor:
        response = cursor.execute(''' UPDATE bakery_items SET discount_percent=%s WHERE item_name=%s; ''', [discount_value, item_name])
    if response:
        return True
    else:
        return False

################################ CUSTOMER's functions #############################################

def checkRegistration(full_name, mobile_no, email_id):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM registered_customers WHERE full_name=%s AND mobile_no=%s AND email_id=%s; ''', [full_name, mobile_no, email_id])
        if cursor.rowcount > 0:
            response = dictfetchone(cursor)
            if full_name == response['full_name'] and mobile_no == response['mobile_no'] and email_id == response['email_id']:
                return True
    return False

def registerUser(full_name, mobile_no, email_id, address, password):
    with connection.cursor() as cursor:
        response = cursor.execute('''INSERT INTO registered_customers(full_name, mobile_no, email_id, address, password) VALUES (%s, %s, %s, %s, %s); ''', [full_name, mobile_no, email_id, address, password])
    if response:
        return True
    else:
        return False

def checkIfRegistered(email_id, password):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM registered_customers WHERE email_id=%s AND password=%s; ''', [email_id, password])
        if cursor.rowcount > 0:
            response = dictfetchone(cursor)
            if response:
                return True
    return False

def checkUserExistence(full_name, mobile_no):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM registered_customers WHERE full_name=%s AND mobile_no=%s; ''', [full_name, mobile_no])
        response = dictfetchone(cursor)
        if cursor.rowcount > 0:
            response = dictfetchone(cursor)
            if response:
                return True
    return False

def fetchSellingPrice(item):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT selling_price FROM bakery_items WHERE item_name=%s; ''', [item])
        if cursor.rowcount > 0:
            response = dictfetchone(cursor)
            if response:
                return response['selling_price']
    return 0

def createOrder(full_name, mobile_no, order_items, order_quantities, pickup_order_date, pickup_order_time, payment_method, payment_made, total_price, return_amount, order_date, order_time):
    with connection.cursor() as cursor:
        response = cursor.execute('''INSERT INTO bakery_orders(full_name, mobile_no, order_items, order_quantities, pickup_order_date, pickup_order_time, payment_method, payment_made, total_price, return_amount, order_date, order_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s); ''', [full_name, mobile_no, order_items, order_quantities, pickup_order_date, pickup_order_time, payment_method, payment_made, total_price, return_amount, order_date, order_time])
    if response:
        return True
    else:
        return False

def getBill(full_name, mobile_no, order_items, order_quantities, pickup_order_date):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM bakery_orders WHERE full_name=%s AND mobile_no=%s AND order_items=%s AND order_quantities=%s AND pickup_order_date=%s; ''', [full_name, mobile_no, order_items, order_quantities, pickup_order_date])
        if cursor.rowcount > 0:
            response = dictfetchall(cursor)
            if response:
                return response[len(response)-1]
        return False

def checkUserOrders(full_name, mobile_no):
    with connection.cursor() as cursor:
        cursor.execute(''' SELECT * FROM bakery_orders WHERE full_name=%s AND mobile_no=%s; ''', [full_name, mobile_no])
        response = dictfetchall(cursor)
    if response:
        return response
    else:
        return False

#SELECT * FROM `bakery_orders` WHERE order_items REGEXP 'Pastry*';