def func(n):
  if n==0: 
    result =1 
  elif n==1: 
    result =1 
  else:
    result = func(n-1) + func(n-2)
  return result 

i =0
sum =0 
while(1):
  if func(i)<=4000000: 
    if func(i)%2 ==0: 
      sum +=func(i)
  else:
    break
  i+=1

print(sum)