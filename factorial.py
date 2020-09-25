#n = int(input("enter a number"))
f=open("result1.txt","a")
def fact(n):
    f.write("factorial=")
    fac = 1
    for i in range(1, n+1):
        fac = fac*i
    f.write(str(fac))
    f.write("\n")
    f.close()

