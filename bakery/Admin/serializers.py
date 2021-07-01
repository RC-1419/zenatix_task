from rest_framework import serializers

class add_ingredientsSerializer(serializers.Serializer):
    ingredient_name = serializers.CharField(required=True)
    quantity = serializers.IntegerField(required=True, min_value=1, max_value=100)
    class Meta:
        fields = '__all__'

class createBakeryItemSerializer(serializers.Serializer):
    BakeryItem_name = serializers.CharField(required=True)
    ingredient_list = serializers.CharField(required=True)
    cost_price = serializers.FloatField(required=True)
    selling_price = serializers.FloatField(required=True)
    ingredient_quantity = serializers.CharField(required=True)
    BakeryItem_quantity = serializers.IntegerField(required=True, min_value=1, max_value=100)
    class Meta:
        fields = '__all__'

class detailOfBakeryItemSerializer(serializers.Serializer):
    BakeryItem_name = serializers.CharField(required=True)
    class Meta:
        fields = '__all__'

class manageInventorySerializer(serializers.Serializer):
    old_item_name = serializers.CharField(default='')
    new_item_name = serializers.CharField(default='')
    item_name = serializers.CharField(default='')
    old_ingredient_name = serializers.CharField(default='')
    new_ingredient_name = serializers.CharField(default='')
    ingredient_name = serializers.CharField(default='')
    quantity = serializers.IntegerField(default=0, min_value=1, max_value=100)
    cost_price = serializers.FloatField(default=0.0)
    selling_price = serializers.FloatField(default=0.0)
    option = serializers.CharField(default='')
    discount_percent = serializers.FloatField(default=0.0)
    class Meta:
        fields = '__all__'

