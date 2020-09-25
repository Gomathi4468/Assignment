#n=int(input("enter a number"))
f=open("result1.txt","a")
def ser(n):
    f.write("series \n")
    for i in range(1,n+1):
        if (i % 2) == 0:
            f.write(str(i))
            f.write("\n")
    f.close()
