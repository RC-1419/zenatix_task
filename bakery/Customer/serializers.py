from rest_framework import serializers

class login_registerSerializer(serializers.Serializer):
    Full_name = serializers.CharField(default='')
    Country_code = serializers.CharField(default='')
    Mobile_no = serializers.IntegerField(default=0)
    Email_id = serializers.CharField(default='')
    Address = serializers.CharField(default='')
    Password = serializers.CharField(default='')
    Confirm_Password = serializers.CharField(default='')
    class Meta:
        fields = '__all__'

class placeAnOrderAndGetBillSerializer(serializers.Serializer):
    Full_name = serializers.CharField(required=True)
    Mobile_no = serializers.IntegerField(required=True, min_value=6000000000, max_value=9999999999)
    Order_items = serializers.CharField(required=True)
    Order_quantities = serializers.CharField(required=True)
    Pickup_Order_Date = serializers.CharField(required=True)
    Pickup_Order_Time = serializers.CharField(default='')
    Payment_method = serializers.CharField(required=True)
    Payment_paid = serializers.IntegerField(required=True)
    class Meta:
        fields = '__all__'

class order_historySerializer(serializers.Serializer):
    Full_name = serializers.CharField(required=True)
    Mobile_no = serializers.IntegerField(required=True, min_value=6000000000, max_value=9999999999)
    class Meta:
        fields = '__all__'