''' Write a Python program that accepts a list of integers and calculates the length and the fifth element. Return true if the length of the list is 8 and the fifth element occurs thrice in the said list.
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True'''

def occurrences_2(arr):
  len_arr = len(arr)
  elem_5 = arr[4]
  occ = arr.count(elem_5)
  if len_arr == 8 and occ == 3:
    return True
  else:
    return False

ejemplo_1 = [19, 19, 15, 5, 5, 5, 1, 2]
resultado_1 = occurrences_2(ejemplo_1)
print(resultado_1)
ejemplo_2 = [19, 15, 5, 7, 5, 5, 2]
resultado_2 = occurrences_2(ejemplo_2)
print(resultado_2)