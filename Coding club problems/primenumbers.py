count=0
for a in range(2,101):
    for i in range(2,a):
        if a%i==0:
            break
    else:
        print(a,"is prime")
        count +=1

print("Total count is ",count)
