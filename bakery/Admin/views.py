from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from . import serializers
import sys
sys.path.append('..')
from workings import return_data, checkIngredientExists, insertItem, checkIngredients, createItem, checkItem, getItemDetails, updateItemName, updateItemDetails, deleteItemDetails, getAllItemDetails, checkIngredient, updateIngredientName, updateIngredientDetails, deleteIngredientDetails, getAllIngredientDetails, findPopularProducts, findPopularityOfItem, updateDiscount
# Create your views here.

@api_view(['POST'])
def add_ingredients(request):
    try:

        serializer = serializers.add_ingredientsSerializer(data=request.data)

        if serializer.is_valid():
            ingredient = serializer['ingredient_name'].value
            quantity = serializer['quantity'].value

            if ingredient and quantity:
                ingredient_exists = checkIngredientExists(ingredient)

                if ingredient_exists == False:
                    item_inserted = insertItem(ingredient, quantity)

                    if item_inserted:
                        return Response(return_data('success', '200', '', 'Ingredient has been added to Bakery.', '0'))

                    else:
                        return Response(return_data('success', '200', '', 'Some error occured while adding the Ingredient to Bakery.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'Ingredient already exists.', '0'))

            else:
                return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['POST'])
def createBakeryItem(request):
    try:

        serializer = serializers.createBakeryItemSerializer(data=request.data)

        if serializer.is_valid():
            item_name = serializer['BakeryItem_name'].value
            item_quantity = serializer['BakeryItem_quantity'].value
            cost_price = serializer['cost_price'].value
            selling_price = serializer['selling_price'].value
            quantity = serializer['ingredient_quantity'].value
            quantity_list_array = [i.strip() for i in quantity.split(',')]
            ingredient_list = serializer['ingredient_list'].value
            ingredient_list_array = [i.strip() for i in ingredient_list.split(',')]

            if item_name and ingredient_list and selling_price and cost_price and quantity and item_quantity:
                cnt = 0
                for ingredient in ingredient_list_array:
                    ingredient_exists = checkIngredients(ingredient)
                    if ingredient_exists:
                        cnt += 1
                        
                if cnt == len(ingredient_list_array) and len(quantity_list_array) == len(ingredient_list_array):
                    item_exists = checkItem(item_name)

                    if not item_exists:
                        created = createItem(item_name, item_quantity, ingredient_list, ingredient_list_array, quantity, cost_price, selling_price)

                        if created:
                            return Response(return_data('success', '200', '', 'Ingredient has been added to Bakery.', '0'))

                        else:
                            return Response(return_data('fail', '400', '', 'Item is not created due to a problem.', '0'))

                    else:
                        return Response(return_data('fail', '400', '', 'Item is already present in the inventory.', '0'))    

                else:
                    return Response(return_data('fail', '400', '', 'Some ingredients from the list are not in the inventory.', '0'))
            
            else:
                return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['POST'])
def detailOfBakeryItem(request):
    try:

        serializer = serializers.detailOfBakeryItemSerializer(data=request.data)

        if serializer.is_valid():
            item_name = serializer['BakeryItem_name'].value

            if item_name:
                item_exists = checkItem(item_name)

                if item_exists:
                    details = getItemDetails(item_name)

                    if details:
                        return Response(return_data('success', '200', details, 'Item details found.', '0'))

                    else:
                        return Response(return_data('fail', '400', '', 'No details found.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such item in the inventory.', '0'))
            
            else:
                return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))    

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))


@api_view(['POST'])
def manageInventory(request):
    try:

        serializer = serializers.manageInventorySerializer(data=request.data)

        if serializer.is_valid():
            old_item_name = serializer['old_item_name'].value
            new_item_name = serializer['new_item_name'].value
            item_name = serializer['item_name'].value
            quantity = serializer['quantity'].value
            cost_price = serializer['cost_price'].value
            selling_price = serializer['selling_price'].value
            old_ingredient_name = serializer['old_ingredient_name'].value
            new_ingredient_name = serializer['new_ingredient_name'].value
            ingredient_name = serializer['ingredient_name'].value
            option = serializer['option'].value
            option = option.lower()
            discount_value = serializer['discount_percent'].value
            
            if old_item_name and new_item_name and option == 'update':
                item_exists = checkItem(old_item_name)
                
                if item_exists:
                    updated = updateItemName(old_item_name, new_item_name)

                    if updated:
                        return Response(return_data('success', '200', '', 'Item name has been updated successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Item name HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such item in the inventory.', '0'))

            elif item_name and option == 'update':
                item_exists = checkItem(item_name)

                if item_exists:
                    updated = updateItemDetails(item_name ,quantity, cost_price, selling_price)

                    if updated:
                        return Response(return_data('success', '200', '', 'Item details has been updated successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Item details HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such item in the inventory.', '0'))

            elif item_name and option == 'delete':
                item_exists = checkItem(item_name)

                if item_exists:
                    deleted = deleteItemDetails(item_name, quantity, cost_price, selling_price)

                    if deleted:
                        return Response(return_data('success', '200', '', 'Item details has been deleted successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Item details HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such item in the inventory.', '0'))
            
            elif option == 'get_items':
                display = getAllItemDetails()

                if display:
                    return Response(return_data('success', '200', display, 'All items details are fetched successfully.', '0'))
                    
                else:
                    return Response(return_data('fail', '400', '', 'Item details are not fetched successfully.', '0'))
            
            elif old_ingredient_name and new_ingredient_name and option == 'update':
                ingredient_exists = checkIngredient(old_ingredient_name)

                if ingredient_exists:
                    updated = updateIngredientName(old_ingredient_name, new_ingredient_name)

                    if updated:
                        return Response(return_data('success', '200', '', 'Ingredient name has been updated successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Ingredient name HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such ingredient in the inventory.', '0'))

            elif ingredient_name and option == 'update':
                ingredient_exists = checkIngredient(ingredient_name)

                if ingredient_exists:
                    updated = updateIngredientDetails(ingredient_name ,quantity)

                    if updated:
                        return Response(return_data('success', '200', '', 'Ingredient details has been updated successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Ingredient details HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such ingredient in the inventory.', '0'))

            elif ingredient_name and option == 'delete':
                ingredient_exists = checkIngredient(ingredient_name)

                if ingredient_exists:
                    deleted = deleteIngredientDetails(ingredient_name, quantity)

                    if deleted:
                        return Response(return_data('success', '200', '', 'Ingredient details has been deleted successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Ingredient details HAS NOT been updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such ingredient in the inventory.', '0'))

            elif option == 'get_ingredients':
                display = getAllIngredientDetails()

                if display:
                    return Response(return_data('success', '200', display, 'All ingredients details are fetched successfully.', '0'))
                    
                else:
                    return Response(return_data('fail', '400', '', 'Ingredient details are not fetched successfully.', '0'))

            elif item_name and discount_value and option == 'discount':
                item_exists = checkItem(item_name)

                if item_exists:
                    updated = updateDiscount(item_name, discount_value)

                    if updated:
                        return Response(return_data('success', '200', '', 'Discount value is updated successfully.', '0'))
                    
                    else:
                        return Response(return_data('fail', '400', '', 'Discount value was NOT updated.', '0'))

                else:
                    return Response(return_data('fail', '400', '', 'No such item in the inventory.', '0'))

            else:
                popular_selling_product_list = findPopularProducts()

                if popular_selling_product_list:
                    popular_dictionary = dict()

                    for item in popular_selling_product_list:
                        value = findPopularityOfItem(item)
                        if value:
                            popular_dictionary[item] = value 
                        popularProduct = max(popular_dictionary, key=popular_dictionary.get)
                    return Response(return_data('success', '200', popularProduct, 'Most popular/Hottest selling product is ' + popularProduct, '0'))
                    
                else:
                    return Response(return_data('fail', '400', '', 'Please fill mandatory field(s)', '0'))  

        else:
            return Response(return_data('fail', '400', '', 'Invalid Serializer', '0'))
    
    except Exception as e:
        print(e)
        return Response(return_data('fail', '400', '', 'Bad Request', '0'))