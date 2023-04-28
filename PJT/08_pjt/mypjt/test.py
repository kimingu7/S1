import csv
import numpy as np
import pandas as pd

def file_open_by_numpy():
    np_arr = np.loadtxt('data/test_data.CSV', delimiter=",", encoding='cp949', dtype=str)
    return np_arr

arr = file_open_by_numpy()

df = pd.DataFrame(arr)

data = df.to_dict('records')

print(data)