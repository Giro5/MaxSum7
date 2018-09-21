a = input()
b = list(sum(list(int(a[x]) for x in range(i*7,i*7+7))) for i in range(len(a)//7))
if len(a)%7!=0:
    b.append(sum(list(int(a[i]) for i in range(len(b)*7,len(a)))))
print(b)
print(max(b))


#for i in range(len(a)//7):
#    b.append(sum(list(int(a[x]) for x in range(i*7,i*7+7))))
