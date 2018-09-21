a = input()
b = []
for i in range(len(a)//7):
    b.append(sum(list(int(a[x]) for x in range(i*6,i*6+7 ) )))
print(b)
print(max(b))
