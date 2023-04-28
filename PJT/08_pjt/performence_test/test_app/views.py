from django.shortcuts import render
from django.http import JsonResponse
import csv
import numpy as np
import pandas as pd
from rest_framework.decorators import api_view
# import random

# array_length = 1000
# random_range = 5000

# @api_view(['GET'])
# def bubble_sort(request):
#     li = []
#     for i in range(array_length):
#         li.append(random.choice(range(1, random_range)))
#     for i in range(len(li) - 1, 0, -1):
#         for j in range(i):
#             if li[j] < li[j + 1]:
#                 li[j], li[j + 1] = li[j + 1], li[j]
#     context = {
#       'top': li[0]
#     }
#     return JsonResponse(context)

# @api_view(['GET'])
# def normal_sort(request):
#     li = []
#     for i in range(array_length):
#         li.append(random.choice(range(1, random_range)))
#     li.sort(reverse=True)
#     context = {
#         'top': li[0]
#     }
#     return JsonResponse(context)

# from queue import PriorityQueue

# @api_view(['GET'])
# def priority_queue(request):
#     pq = PriorityQueue()
#     for i in range(array_length):
#         pq.put(-random.choice(range(1, random_range)))
#     context = {
#         'top': -pq.get()
#     }
#     return JsonResponse(context)


def test_data():
    np_arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr


def c(request):
    arr = test_data()
    columns=arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)
    df['나이'] = pd.to_numeric(df['나이'])
    mean_age = df['나이'].mean()
    df['나이_차이'] = abs(df['나이'] - mean_age)
    df = df.sort_values(by=['나이_차이'])
    df = df.head(10)
    data = df.to_dict('records')
    return JsonResponse({'data': data})