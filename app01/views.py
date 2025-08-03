from rest_framework.views import APIView
from django.shortcuts import render
from .models import Test
from .serializers import TestSerializer
from rest_framework.response import Response

class testView(APIView):
    def get(self, request):
        test1 = Test.objects.all()
        test_ser = TestSerializer(test1, many=True)
        return Response({"code":200, "data":test_ser.data})
    def post(self, request):
        ser = TestSerializer(data=request.data)
        if ser.is_valid():
            ser.create(ser.validated_data)
            return Response({"code":200, "data":ser.data})
        return Response({"code":400, "data":ser.errors})
class testDetailView(APIView):
    def get(self, request, pk):
        test1 = Test.objects.get(id=pk)
        tset_ser = TestSerializer(test1)
        return Response({"code":200, "data":tset_ser.data})
    def put(self, request, pk):
        test1 = Test.objects.get(id=pk)
        ser = TestSerializer(test1, data=request.data)
        if ser.is_valid():
            ser.update(test1, ser.validated_data)
            return Response({"code":200, "data":ser.data})
        return Response({"code":400, "data":ser.errors})    
    def delete(self, request, pk):
        test1 = Test.objects.get(id=pk)
        test1.delete()
        return Response({"code":200, "data":None})
