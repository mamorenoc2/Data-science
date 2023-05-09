def matchingStrings(strings, queries):
  list_maching_strings = []
  for i in range(0,len(queries)):
    list_maching_strings[i].append(0)
    for j in range(0, len(strings)):
      if strings[j] == queries[i]:
        list_maching_strings[i] += 1
      
  return list_maching_strings

strings = ['def', 'de', 'fgh']
queries = ['de', 'lmn', 'fgh']

ejemplo = matchingStrings(strings, queries)