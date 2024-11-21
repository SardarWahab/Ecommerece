from rest_framework.decorators import api_view
from rest_framework.response import Response
from  home.models import Product
from home.serializer import ProductSerializers
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def get_product(request):
    product = Product.objects.all()
    serializer = ProductSerializers(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_single_product(request,id):      
    try:
        product = Product.objects.get(id=id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    except:
        return Response({'message':'product not found'},status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def save_product(request):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    else:
        return Response({"msg":"Something went wrong"}, status=400)

@api_view(['DELETE'])
def delete_product(request,id):
    try:
        product = Product.objects.get(id=id)
        product.delete()
        return Response({"msg":"product deleted"}, status=status.HTTP_200_OK)
    except :
        return Response({"msg":"product not found"}, status=404)
