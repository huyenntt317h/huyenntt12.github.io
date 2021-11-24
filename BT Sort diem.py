#Bài 2: Sorting - Sắp xếp điểm thi
def sort_list_last(list_a):
  list_sorted = sorted(list_a, key=lambda tup:tup[2])
  return list_sorted

A = [(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]
print("Danh sách sau khi sắp xếp: ", sort_list_last(A))
