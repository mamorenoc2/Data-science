def lonelyinteger(a):
    for i in a:
        occurrency = a.count(i)
        if occurrency == 1:
            result = i
    return result

a = [3, 2, 1, 4, 3, 2, 1]
print(lonelyinteger(a))