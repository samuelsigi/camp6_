from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import CustomerSerializer, OrderSerializer, OrderItemSerializer
from .models import Customer, Order, OrderItem
# Create your views here.


@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        customer_list = Customer.objects.all()
        customer_list_serializer = CustomerSerializer(customer_list, many=True)
        return JsonResponse(customer_list_serializer.data, safe=False, status=200)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        customer_add_serializer = CustomerSerializer(data=request_data)
        if customer_add_serializer.is_valid():
            customer_add_serializer.save()
            return JsonResponse(customer_add_serializer.data, status=201)
        return JsonResponse(customer_add_serializer.errors, status=400)


@csrf_exempt
def customer_details_view(request, passed_name):
    try:
        customer_details = Customer.objects.filter(name__icontains=passed_name)
        if not customer_details.exists():
            raise Exception("Not Found")
    except Exception as e:
        return JsonResponse({'Not Found': 'Customer not Found'}, status=404)

    if request.method == "GET":
        customer_details_serializer = CustomerSerializer(customer_details,many=True)
        return JsonResponse(customer_details_serializer.data, safe=False, status=200)

    elif request.method == "PUT":
        requested_data = JSONParser().parse(request)
        customer_update_serializer = (CustomerSerializer(customer_details, data=requested_data))
        if customer_update_serializer.is_valid():
            customer_update_serializer.save()
            return JsonResponse(customer_update_serializer.data, safe=False, status=201)
        return JsonResponse(customer_update_serializer.errors, status=400)

    elif request.method == "DELETE":
        customer_details.delete()
        return HttpResponse(status=204)


@csrf_exempt
def order_list(request):
    if request.method == "GET":
        order_list = Order.objects.all()
        order_list_serializer = OrderSerializer(order_list, many=True)
        return JsonResponse(order_list_serializer.data, safe=False, status=200)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        order_add_serializer = OrderSerializer(data=request_data)
        if order_add_serializer.is_valid():
            order_add_serializer.save()
            return JsonResponse(order_add_serializer.data, status=201)
        return JsonResponse(order_add_serializer.errors, status=400)


@csrf_exempt
def order_details_view(request, passed_id):
    try:
        order_details = Order.objects.filter(id__contains=passed_id)
        if not order_details.exists():
            raise Exception("Not Found")
    except Exception as e:
        return JsonResponse({'Not Found': 'Order not Found'}, status=404)

    if request.method == "GET":
        order_details_serializer = OrderSerializer(order_details,many=True)
        return JsonResponse(order_details_serializer.data, safe=False, status=200)

    elif request.method == "PUT":
        requested_data = JSONParser().parse(request)
        order_update_serializer = (OrderSerializer(order_details, data=requested_data))
        if order_update_serializer.is_valid():
            order_update_serializer.save()
            return JsonResponse(order_update_serializer.data, safe=False, status=201)
        return JsonResponse(order_update_serializer.errors, status=400)

    elif request.method == "DELETE":
        order_details.delete()
        return HttpResponse(status=204)



@csrf_exempt
def order_item_list(request):
    if request.method == "GET":
        order_item_list = OrderItem.objects.all()
        order_item_list_serializer = OrderItemSerializer(order_item_list, many=True)
        return JsonResponse(order_item_list_serializer.data, safe=False, status=200)

    elif request.method == "POST":
        request_data = JSONParser().parse(request)
        order_item_add_serializer = OrderItemSerializer(data=request_data)
        if order_item_add_serializer.is_valid():
            order_item_add_serializer.save()
            return JsonResponse(order_item_add_serializer.data, status=201)
        return JsonResponse(order_item_add_serializer.errors, status=400)


@csrf_exempt
def order_item_details_view(request, passed_item_name):
    try:
        order_item_details = OrderItem.objects.filter(passed_item_name__contains=passed_item_name)
        if not order_item_details.exists():
            raise Exception("Not Found")
    except Exception as e:
        return JsonResponse({'Not Found': 'Order Item not Found'}, status=404)

    if request.method == "GET":
        order_item_details_serializer = OrderItemSerializer(order_item_details,many=True)
        return JsonResponse(order_item_details_serializer.data, safe=False, status=200)

    elif request.method == "PUT":
        requested_data = JSONParser().parse(request)
        order_item_update_serializer = (OrderItemSerializer(order_item_details, data=requested_data))
        if order_item_update_serializer.is_valid():
            order_item_update_serializer.save()
            return JsonResponse(order_item_update_serializer.data, safe=False, status=201)
        return JsonResponse(order_item_update_serializer.errors, status=400)

    elif request.method == "DELETE":
        order_item_details.delete()
        return HttpResponse(status=204)