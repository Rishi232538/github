

a = [1,8,7,6,10,2, 78]
n = len(a)
print(n)
temp = 0

#n-1 = 7 -1 = 6
for i in range(0, n):
    if a[i]>temp:
        temp = a[i]
print(temp)



