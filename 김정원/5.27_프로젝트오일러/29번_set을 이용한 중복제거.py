k = set()
for i in range(2,101):
  for j in range(2,101):
     k.add(i**j)

print(len(k))