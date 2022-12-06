

a = [9,2,7,4,5]
n = len(a)
for i in range(0, n):
    for j in range(i+1, n):
        if a[i]<a[j]:
            temp =a[i]
            a[i] = a[j]
            a[j]=temp
print(a)