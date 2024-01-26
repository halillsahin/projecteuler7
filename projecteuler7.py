a=[2]
n=2
def asalkontrol(x):
    for i in range(2,int((x**0.5)+1)):
        if x%i==0:
             return False
    else:
        return True

     
while True:
    n+=1
    if asalkontrol(n):
         a.append(n)
    else:
         continue     
    if len(a)==10001:
            print(max(a))
            break
   
    
    
        

