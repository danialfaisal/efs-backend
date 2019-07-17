from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly




# now = timezone.now()
# def home(request):
#    return render(request, 'portfolio/home.html',
#                  {'portfolio': home})
#
# @login_required
# def customer_list(request):
#     customer = Customer.objects.filter(created_date__lte=timezone.now())
#     return render(request, 'portfolio/customer_list.html',
#                  {'customers': customer})
#
# @login_required
# def customer_edit(request, pk):
#    customer = get_object_or_404(Customer, pk=pk)
#    if request.method == "POST":
#        # update
#        form = CustomerForm(request.POST, instance=customer)
#        if form.is_valid():
#            customer = form.save(commit=False)
#            customer.updated_date = timezone.now()
#            customer.save()
#            customer = Customer.objects.filter(created_date__lte=timezone.now())
#            return render(request, 'portfolio/customer_list.html',
#                          {'customers': customer})
#    else:
#         # edit
#        form = CustomerForm(instance=customer)
#    return render(request, 'portfolio/customer_edit.html', {'form': form})
#
# @login_required
# def customer_delete(request, pk):
#    customer = get_object_or_404(Customer, pk=pk)
#    customer.delete()
#    return redirect('portfolio:customer_list')
#
# @login_required
# def stock_list(request):
#    stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
#    return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
#
# @login_required
# def stock_new(request):
#    if request.method == "POST":
#        form = StockForm(request.POST)
#        if form.is_valid():
#            stock = form.save(commit=False)
#            stock.created_date = timezone.now()
#            stock.save()
#            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
#            return render(request, 'portfolio/stock_list.html',
#                          {'stocks': stocks})
#    else:
#        form = StockForm()
#        # print("Else")
#    return render(request, 'portfolio/stock_new.html', {'form': form})
#
# @login_required
# def stock_edit(request, pk):
#    stock = get_object_or_404(Stock, pk=pk)
#    if request.method == "POST":
#        form = StockForm(request.POST, instance=stock)
#        if form.is_valid():
#            stock = form.save()
#            # stock.customer = stock.id
#            stock.updated_date = timezone.now()
#            stock.save()
#            stocks = Stock.objects.filter(purchase_date__lte=timezone.now())
#            return render(request, 'portfolio/stock_list.html', {'stocks': stocks})
#    else:
#        # print("else")
#        form = StockForm(instance=stock)
#    return render(request, 'portfolio/stock_edit.html', {'form': form})
#
# @login_required
# def stock_delete(request, pk):
#    stock = get_object_or_404(Stock, pk=pk)
#    stock.delete()
#    return redirect('portfolio:stock_list')
#
# @login_required
# def investment_list(request):
#    investments = Investment.objects.filter(recent_date__lte=timezone.now())
#    return render(request, 'portfolio/investment_list.html', {'investments': investments})
#
# @login_required
# def investment_new(request):
#    if request.method == "POST":
#        form = InvestmentForm(request.POST)
#        if form.is_valid():
#            investment = form.save(commit=False)
#            investment.created_date = timezone.now()
#            investment.save()
#            investments = Investment.objects.filter(acquired_date__lte=timezone.now())
#            return render(request, 'portfolio/investment_list.html',
#                          {'investments': investments})
#    else:
#        form = InvestmentForm()
#        # print("Else")
#    return render(request, 'portfolio/investment_new.html', {'form': form})
#
# @login_required
# def investment_edit(request, pk):
#    investment = get_object_or_404(Investment, pk=pk)
#    if request.method == "POST":
#        form = InvestmentForm(request.POST, instance=investment)
#        if form.is_valid():
#            investment = form.save()
#            # investment.customer = investment.id
#            investment.updated_date = timezone.now()
#            investment.save()
#            investments = Investment.objects.filter(acquired_date__lte=timezone.now())
#            return render(request, 'portfolio/investment_list.html', {'investments': investments})
#    else:
#        # print("else")
#        form = InvestmentForm(instance=investment)
#    return render(request, 'portfolio/investment_edit.html', {'form': form})
#
# @login_required
# def investment_delete(request, pk):
#    investment = get_object_or_404(Investment, pk=pk)
#    investment.delete()
#    return redirect('portfolio:investment_list')
#
# @login_required
# def portfolio(request,pk):
#    customer = get_object_or_404(Customer, pk=pk)
#    customers = Customer.objects.filter(created_date__lte=timezone.now())
#    investments =Investment.objects.filter(customer=pk)
#    stocks = Stock.objects.filter(customer=pk)
#    sum_recent_value = Investment.objects.filter(customer=pk).aggregate(Sum('recent_value'))
#    sum_acquired_value = Investment.objects.filter(customer=pk).aggregate(Sum('acquired_value'))
#    #overall_investment_results = sum_recent_value-sum_acquired_value
#    # Initialize the value of the stocks
#    sum_current_stocks_value = 0
#    sum_of_initial_stock_value = 0
#
#    #***** Currency Layer Code *********************************
#    convert_base_url = 'http://apilayer.net/api/live?access_key='
#    convert_api_key = 'c6e55388423a859272fe982e5546ca9a'
#    base_currency = '&source=USD'
#    convert_currency = '&currencies=EUR'
#    convert_format = '&format=1'
#    convert_url = convert_base_url+convert_api_key+convert_currency+base_currency+convert_format
#    rates = requests.get(convert_url).json()
#    eur_conv_rate = rates["quotes"]["USDEUR"]
#    #****** Currency Layer Code **********************************
#
#    # Loop through each stock and add the value to the total
#    for stock in stocks:
#         sum_current_stocks_value += stock.current_stock_value()
#         sum_of_initial_stock_value += stock.initial_stock_value()
#
#    return render(request, 'portfolio/portfolio.html', {'customers': customers,
#                                                        'investments': investments,
#                                                        'stocks': stocks,
#                                                        'sum_acquired_value': sum_acquired_value,
#                                                        'sum_recent_value': sum_recent_value,
#                                                        'sum_current_stocks_value': sum_current_stocks_value,
#                                                        'sum_of_initial_stock_value': sum_of_initial_stock_value,
#                                                        'eur_conv_rate': eur_conv_rate})
#
# # Lists all customers
# class CustomerList(APIView):
#
#     def get(self,request):
#         customers_json = Customer.objects.all()
#         serializer = CustomerSerializer(customers_json, many=True)
#         return Response(serializer.data)



@csrf_exempt
@api_view(['GET', 'POST'])
def customer_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getCustomer(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        customer = Customer.objects.get(pk=pk)
    except Customer.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CustomerSerializer(customer,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CustomerSerializer(customer, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def investment_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        investment = Investment.objects.all()
        serializer = InvestmentSerializer(investment, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = InvestmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getInvestment(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        investment = Investment.objects.get(pk=pk)
    except Investment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = InvestmentSerializer(investment,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = InvestmentSerializer(investment, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        investment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
@api_view(['GET', 'POST'])
def stock_list(request):
    permission_classes = (IsAuthenticatedOrReadOnly)
    if request.method == 'GET':
        stock = Stock.objects.all()
        serializer = StockSerializer(stock, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def getStock(request, pk):
    """
    Retrieve, update or delete a customer instance.
    """
    try:
        stock = Stock.objects.get(pk=pk)
    except Stock.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StockSerializer(stock,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StockSerializer(stock, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

