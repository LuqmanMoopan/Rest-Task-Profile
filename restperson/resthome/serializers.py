from rest_framework import serializers
from resthome.models import Person, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class PersonSerializer(serializers.ModelSerializer):
    address = AddressSerializer()

    class Meta:
        model = Person
        fields = '__all__'

    def create(self, validated_data):
        address_data = validated_data.pop('address')
        address_instance = Address.objects.create(**address_data)
        person_instance = Person.objects.create(address=address_instance, **validated_data)
        return person_instance
    
    def update(self, instance, validated_data):
        address_data = validated_data.pop('address', None)
        if address_data:
            address_instance = instance.address
            address_serializer = AddressSerializer(instance=address_instance, data=address_data)
            if address_serializer.is_valid():
                address_serializer.save()
        return super().update(instance, validated_data)
