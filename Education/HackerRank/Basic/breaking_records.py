def breakingRecords(scores):
    scores_actual = 0
    min_n = 0
    max_n = 0
    min_m = scores[0]
    max_m = scores[0]
    list_m = []
    for i in range(0,len(scores)):
        scores_actual = scores[i]
      
        if scores_actual < min_m:
            min_m = scores_actual
            min_n += 1
        if scores_actual > max_m:
            max_m = scores_actual
            max_n += 1
    list_m.append(max_n)
    list_m.append(min_n)
    return list_m

example = breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1])
print(example)