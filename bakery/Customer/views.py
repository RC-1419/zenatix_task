from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from . import serializers
import sys, datetime
sys.path.append('..')
from workings import return_data, checkRegistration, registerUser, getAllItemDetails, checkIfRegistered, checkUserExistence, fetchSellingPrice, createOrder, getBill, checkUserOrders
# Create your views here.

@api_view(['POST'])
def login_register(request):
    try:

        serializer = serializers.login_registerSerializer(data=request.data)

        if serializer.is_valid():
            full_name = serializer['Full_name'].value
            mobile_no = serializer['Mobile_no'].value
            email_id = serializer['Email_id'].value
            address = serializer['Address'].value
            password = serializer['Password'].value
            confirm_password = serializer['Confirm_Password'].value

            if full_name and mobile_no and email_id and address and password and confirm_password:
                already_registered = checkRegistration(full_name, mobile_no, email_id)
                
                if already_registered == False:

                    if password == confirm_password:
                        inserted = registerUser(full_name, mobile_no, email_id, address, password)
                        
                        if inserted:
                            return Response(return_data('success', '200', '', 'You are registered successfully. Welcome to the bakery!', '0'))
                        
                        else:
                            return Response(return_data('fail', '400', '', 'Your registration was NOT successful. Try again!!', '0'))

                    else:
                        return Response(return_data('fail', '400', '', 'Password and Confirm_Password are not same', '0'))  

                else:
                    return Response(return_data('fail', '300', '', 'A user with same name and mobile number already exists.', '0'))
            
            elif email_id and password:
                user_exists = checkIfRegistered(email_id, password)

                if user_exists:
                    return Response(return_data('success', '200', '', 'Login successful. Welcome to the bakery!', '0'))
                        
                else:
                    return Response(return_data('fail', '400', '', 'Invalid Email_Id or Password. Try again!!', '0'))

            else:
                return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['GET'])
def available_products(request):
    try:

        products = getAllItemDetails()

        if products:
            return Response(return_data('success', '200', products, 'List of all available products in the bakery.', '0'))
                
        else:
            return Response(return_data('fail', '300', '', 'No products are avialable in the bakery.', '0'))

    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['POST'])
def placeAnOrderAndGetBill(request):
    try:

        serializer = serializers.placeAnOrderAndGetBillSerializer(data=request.data)

        if serializer.is_valid():
            full_name = serializer['Full_name'].value
            mobile_no = serializer['Mobile_no'].value
            order_items = serializer['Order_items'].value
            order_quantities = serializer['Order_quantities'].value
            pickup_order_date = serializer['Pickup_Order_Date'].value
            pickup_order_time = serializer['Pickup_Order_Time'].value
            payment_method = serializer['Payment_method'].value
            payment_made = serializer['Payment_paid'].value

            if ',' in order_items and ',' in order_quantities:
                order_items_list = [i.strip() for i in order_items.split(',')]
                order_quantities_list = [i.strip() for i in order_quantities.split(',')]

                if len(order_items_list) == len(order_quantities_list):

                    if full_name and mobile_no and order_items and order_quantities and pickup_order_date and payment_method and payment_made:
                        cost_dictionary, combined_list, total_price = dict(), dict(), 0
                        
                        for i in range(len(order_items_list)):
                            combined_list[order_items_list[i]] = order_quantities_list[i]

                        for item in order_items_list:
                            value_exists = fetchSellingPrice(item)
                            if value_exists:
                                cost_dictionary[item] = value_exists
                            else:
                                return Response(return_data('fail', '400', '', 'One or more of your ordered item(s) is not available in the inventory of the bakery.', '0'))   
                        
                        for i,j in combined_list.items():
                            total_price += float(j) * cost_dictionary[i]

                        if total_price < payment_made:
                            return_amount = payment_made - total_price
                            order_date = str(datetime.datetime.now()).split(' ')[0]
                            order_time = str(datetime.datetime.now()).split(' ')[1]
                            created_order = createOrder(full_name, mobile_no, order_items, order_quantities, pickup_order_date, pickup_order_time, payment_method, payment_made, total_price, return_amount, order_date, order_time)
                            
                            if created_order:
                                bill = getBill(full_name, mobile_no, order_items, order_quantities, pickup_order_date)

                                if bill:
                                    return Response(return_data('success', '200', bill, 'Order Successful!! THANK YOU for shopping from our bakery!! Here is your bill.', '0'))
                                
                                else:
                                    return Response(return_data('fail', '400', '', 'Your bill is NOT created successfully.', '0'))   

                            else:
                                return Response(return_data('fail', '400', '', 'Your order was NOT created successfully.', '0'))   

                        else:
                            return Response(return_data('fail', '400', '', 'You have paid less amount than the total amount of your order!', '0'))   
                            
                    else:
                        return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

                else:
                    return Response(return_data('fail', '400', '', 'Total number of products and their quatities provided should be equal.', '0'))

            else:
                if full_name and mobile_no and order_items and order_quantities and pickup_order_date and payment_method and payment_made:
                    cost_dictionary, combined_list, total_price = dict(), dict(), 0
                    
                    combined_list[order_items] = order_quantities

                    value_exists = fetchSellingPrice(order_items)
                    if value_exists:
                        cost_dictionary[order_items] = value_exists
                    
                        for i,j in combined_list.items():
                            total_price += float(j) * cost_dictionary[i]
                        
                        if total_price < payment_made:
                            return_amount = payment_made - total_price
                            order_date = str(datetime.datetime.now()).split(' ')[0]
                            order_time = str(datetime.datetime.now()).split(' ')[1]
                            created_order = createOrder(full_name, mobile_no, order_items, order_quantities, pickup_order_date, pickup_order_time, payment_method, payment_made, total_price, return_amount, order_date, order_time)
                            
                            if created_order:
                                bill = getBill(full_name, mobile_no, order_items, order_quantities, pickup_order_date)

                                if bill:
                                    return Response(return_data('success', '200', bill, 'Order Successful!! THANK YOU for shopping from our bakery!! Here is your bill.', '0'))
                                
                                else:
                                    return Response(return_data('fail', '400', '', 'Your bill is NOT created successfully.', '0'))   

                            else:
                                return Response(return_data('fail', '400', '', 'Your order was NOT created successfully.', '0'))   

                        else:
                            return Response(return_data('fail', '400', '', 'You have paid less amount than the total amount of your order!', '0'))   
                        
                    else:
                        return Response(return_data('fail', '400', '', 'Your ordered item is not available in the inventory of the bakery.', '0'))   

                else:
                    return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    
            
        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['POST'])
def order_history(request):
    try:

        serializer = serializers.order_historySerializer(data=request.data)

        if serializer.is_valid():
            full_name = serializer['Full_name'].value
            mobile_no = serializer['Mobile_no'].value

            if full_name and mobile_no:
                orders = checkUserOrders(full_name, mobile_no)

                if orders:
                    return Response(return_data('success', '200', orders, 'Here is a list of all your orders.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'You have no order history in our bakery.', '0'))    

            else:
                return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))