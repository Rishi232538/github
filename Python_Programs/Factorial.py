
#5*4*3*2*1

#fact(3) - > 5* fact(2)
#fact(2) - > 5* fact(1)
#fact(1) - > 5* fact(0)

def fact(num):
    if num ==0:
        return 1
    else:
        return num*fact(num-1)
    
print(fact(3))





