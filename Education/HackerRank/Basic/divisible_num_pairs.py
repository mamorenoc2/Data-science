def divisibleSumPairs(n, k, ar):
  # Write your code here
  sum_arr = 0
  num_pairs = 0
  for i in range(0, n):
    j = i + 1
    while j < n:
      sum_arr = ar[i] + ar[j]
      divisor = sum_arr % k
      if divisor == 0:
        num_pairs += 1
      j += 1
  return num_pairs
example = divisibleSumPairs(6, 5, [1, 2, 3, 4, 5, 6])
print(example)