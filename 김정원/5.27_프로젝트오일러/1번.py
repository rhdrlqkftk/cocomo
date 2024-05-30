i =0
sum =0 
while(1): 
  if i >= 1000:
    break
  elif(i%3)== 0 or (i%5)==0 :
    sum += i
  i+=1
print(sum)