l1 = list(map(int,input("Enter list value with space:").split()))
l2 = list(map(int,input("Enter list value with space:").split()))

ls = []

for i in range(len(l1)):
    if l1[i]%2!=0:
        ls.append(l1[i])

for j in range(len(l2)):
    if l2[j]%2 == 0:
        ls.append(l2[j])
print(ls)

#OR

newlist = [(l1[i]) for i in range(len(l1)) if l1[i]%2!=0] + [(l2[j]) for j in range(len(l2)) if l2[j]%2==0]
print(newlist)
