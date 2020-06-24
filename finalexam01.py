b=0
for i in range(1,902,100):
    for a in range(1,i):
        c=int(4*((-1)(**int(a+1))/(2*i-1)))
        b+=int(c)
    print("i m(i)")
    print(i,b)