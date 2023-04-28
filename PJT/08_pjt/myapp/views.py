from django.shortcuts import render
from django.http import JsonResponse
import csv
import numpy as np
import pandas as pd

# Create your views here.
def test_data():
    np_arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

def test_data_has_null():
    np_arr = np.loadtxt('data/test_data_has_null.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

def a(request):
    arr = test_data()
    columns=arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)
    data = df.to_dict('records')

    return JsonResponse({'data': data})

def b(request):
    arr = test_data_has_null()
    columns=arr[0]
    arr = np.delete(arr, 0, 0)
    df = pd.DataFrame(arr, columns=columns)
    df.replace("", "NULL", inplace=True)
    data = df.to_dict('records')

    return JsonResponse({'data': data})

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