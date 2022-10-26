a=int(input())
b=int(input())
c=int(input())
for i in range(c):
    if i % a == 0 and i % b == 0:
        print ('FB')
    elif i % a == 0:
        print ('F')
    elif i % b == 0:
        print ('B')
    else:
        print (i)