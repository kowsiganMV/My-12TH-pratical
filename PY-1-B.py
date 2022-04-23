num=int(input("Enter a valueof num:"))
s=0.0
for i in range(1,num+1):
    a=float(i**i)/i
    s=a+s
print("The sum of the series is:",s)
