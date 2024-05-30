max =0 

for i in range(100,1000):
  for j in range(100,1000):
    k = str(i * j)
    if(len(k) >= 6):
      a,b,c,d,e,f = k[0],k[1],k[2],k[3],k[4],k[5]
      if a==f and b ==e and c==d:
        if max < int(k):
          max = int(k)
print(max)