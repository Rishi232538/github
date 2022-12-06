
str_ip = "A,B,C,D,E,F"
str= ''

for i in str_ip:
    if i == ',':
        continue
    str = str + i
    ele = str.split()
print(ele)



