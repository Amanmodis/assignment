from rest_framework import serializers
from test.models import default

class khataserializer(serializers.ModelSerializer):
    class Meta:
        model = default
        fields =  "__all__"       
        
        