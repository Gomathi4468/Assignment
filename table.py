#n=int(input("enter a number:"))
f=open("result1.txt","a")
def tab(n):
    f.write("table \n")
    for i in range(1, 11):
        f.write(str(n))
        f.write("x")
        f.write(str(i))
        f.write("=")
        f.write(str(n*i))
        f.write("\n")
    f.close()
