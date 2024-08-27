n = int(input('Вводим число:  '))
result = []
for i in range(1,n):
    for j in range(i,n):
        if j!= i :
            if n % (i + j) == 0:
                result.append(i) , result.append(j)
print(result)