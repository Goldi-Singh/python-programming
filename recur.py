#using loop

def mul(a,b):
    result=0

    for i in range(b):
     
     result=result+a
    print(result)
mul(3,4);
#using recursion
def mul(a,b):
   if b==1:
      return a;
   else:
      return a+mul(a,b-1)
print(mul(3,4))
