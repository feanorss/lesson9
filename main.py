list=list(range(100,999))
b=0
for i in list:
  a = str(i)
  if a[0] != a[1] and a[1] != a[2] and a[0] != a[2] or (a[0] == a[1] and a[1] == a[2] and a[0] == a[2]):
  b=b+1,
print(b)
