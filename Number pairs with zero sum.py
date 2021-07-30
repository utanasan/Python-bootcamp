l1=[2,4,-5,6,8,-2]
l2=[2,-6,8,3,5,-2]

l3=[]
for i in l1:
    for j in l2:
        if i+j==0:
            l3.append((i,j))
print(l3)

# OR

l4 = [(i,j) for i in l1 for j in l2 if i+j==0]
print(l4)