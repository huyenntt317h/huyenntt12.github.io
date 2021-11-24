#Bài 1: Function - Chỉ số thống kê mô tả
# Hàm 1: Tính giá trị trung bình (mean) của list
def mean(list_data):
    sum_of_data = 0
    for i in list_data:
        sum_of_data += i

    avg = sum_of_data/len(list_data)
    return avg

# Hàm 2: Tính trung vị (median) của list
def median(list_data):
    list_sorted = sorted(list_data)
    len_data = len(list_sorted)
    middle_position = len_data // 2
    if len_data % 2 == 0:
        median_value = (list_sorted[middle_position -1] + list_sorted[middle_position])/2
    else:
        median_value  = list_sorted[middle_position] 
    return median_value

# Hàm 3: Tìm những phần tử có số lần xuất hiện nhiều nhất trong dãy (mode)
from collections import Counter
def mode(list_data):
    counter_values = Counter(list_data)
    max_value = max(counter_values.values())  # maximum value
    max_keys = [k for k,v in counter_values.items() if v== max_value]
    return max_keys

#in ra ket qua        
A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1, 10] 
B=[4,4,5,4,5,5] 
result_A = (mean(A), median(A), mode(A))
result_B = (mean(B), median(B), mode(B))
print(f"A = {A} thì (mean(A), median(A), mode(A)) = {result_A}")
print(f"B = {B} thì (mean(A), median(A), mode(A)) = {result_B}")