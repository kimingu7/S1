from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse, HttpResponse
from django.conf import settings
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DepositProducts, DepositOptions
from django.core import serializers
from .serializers import DepositProductsSerializer, DepositOptionsSerializer

# Create your views here.

BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

API_KEY = settings.API_KEY

# @api_view(['GET'])
# def api_test(request):
#     URL = BASE_URL + 'depositProductsSearch.json'
#     params = {
#         'auth' : settings.API_KEY,
#         'topFinGrpNo' : '020000',
#         'pageNo' : 1,
# 	}
#     response = requests.get(URL, params=params).json()
#     return JsonResponse({ 'response': response })

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth': settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1,
    }
    response = requests.get(URL, params=params).json()
    deposit_products = response['result']['baseList']
    deposit_products_options = response['result']['optionList']

    for product in deposit_products:
        deposit_product = DepositProducts(
            fin_prdt_cd=product['fin_prdt_cd'],
            kor_co_nm=product['kor_co_nm'],
            fin_prdt_nm=product['fin_prdt_nm'],
            etc_note=product['etc_note'],
            join_deny=product['join_deny'],
            join_member=product['join_member'],
            join_way=product['join_way'],
            spcl_cnd=product['spcl_cnd'],
        )
        deposit_product.save()

    for option in deposit_products_options:
        fin_prdt_cd = DepositProducts.objects.get(fin_prdt_cd=option['fin_prdt_cd'])
        deposit_products_option = DepositOptions(
            fin_prdt_cd=fin_prdt_cd,
            intr_rate_type_nm=option['intr_rate_type_nm'],
            intr_rate=option['intr_rate'],
            intr_rate2=option['intr_rate2'],
            save_trm=option['save_trm'],
        )
        deposit_products_option.save()

    deposit_products = DepositProducts.objects.all()
    serializer = DepositProductsSerializer(deposit_products, many=True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):
    deposit_product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(deposit_product.depositoptions_set.all(), many=True)
    return Response(serializer.data)

@api_view(['GET'])
def top_rate(request):
    top_option = DepositOptions.objects.order_by('-intr_rate2').first()
    top_product = top_option.fin_prdt_cd
    option_list = DepositOptions.objects.filter(fin_prdt_cd=top_product)

    result = {
        'top_product': DepositProductsSerializer(top_product).data,
        'top_option': DepositOptionsSerializer(top_option).data,
    }

    return Response(result)
