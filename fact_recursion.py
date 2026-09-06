def fact(num):
    res = 1
    for i in range(1, num+1):
        res = res * i
    return res

print(fact(5))

#recussion
def recursion_fact(num):
    if num == 1:
        return 1
    else:
        return num * recursion_fact(num -1)

print(recursion_fact(12))