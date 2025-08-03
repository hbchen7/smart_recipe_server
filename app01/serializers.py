from rest_framework import serializers
from app01.models import *

# class TestSerializer(serializers.Serializer
# ):
#   id = serializers.IntegerField(read_only=True)
#   name = serializers.CharField()
#   age = serializers.IntegerField()
#   def create(self, validated_data):
#     return Test.objects.create(**validated_data)
#   def update(self, instance, validated_data):
#     instance.name = validated_data.get('name', instance.name)
#     instance.age = validated_data.get('age', instance.age)
#     instance.save()
#     return instance

class TestSerializer(serializers.ModelSerializer):
  class Meta:
    model = Test
    exclude = ['id']
