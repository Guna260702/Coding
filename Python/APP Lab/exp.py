def fact(a):
    if a==0 or a==1:
        return 1
    elif a<0:
        return 'No factorial for negative numbers'
    else:
        return a*fact(a-1)

print(fact(1))