list1=[i for i in range(10,0,-1)]
print(list1)
for j,i in enumerate(list1):
    if i%2==1:
        del list1[j]
print(list1)


