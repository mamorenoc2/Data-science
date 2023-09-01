''' Write a Python program to find a list of integers with exactly two occurrences of nineteen and at least three occurrences of five. Return True otherwise False.
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True'''

def occurrences(arr):
  n_5 = 0
  n_19 = 0
  for i in arr:
    if i == 5:
      n_5 += 1
    elif i == 19:
      n_19 += 1
  if (n_5 == 3 and n_19 == 2):
    return True
  else:
    return False

ejemplo_1 = [19, 19, 15, 5, 3, 5, 5, 2]
resultado_1 = occurrences(ejemplo_1)
ejemplo_2 = [19, 15, 15, 5, 3, 3, 5, 2]
resultado_2 = occurrences(ejemplo_2)
print(resultado_1)
print(resultado_2)