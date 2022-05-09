def multiply(a):
    answer = 1
    for j in lst:
        answer *= j
    return answer


n = int(input("n = "))
lst = []
for i in range(2, n + 1):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)
print(lst)
z = int(input("\n1 сумма\n2 умножение\n"))
if z == 1:
    print(sum(lst))
elif z == 2:
    print(multiply(lst))
