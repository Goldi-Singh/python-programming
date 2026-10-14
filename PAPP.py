num=int(input("enter a number of your choice:"))
n=num;
#prime number
if n<=1:
    print("not prime")
else:
    is_prime=True
    for i in range(2,n//2+1):
        if n % i==0:
            is_prime=False;
        break
if is_prime:
    print("is prime number")

else:
    print("not prime number")

# perfetct number
div_sum=0
for i in range(1,n-1):
    
    if n % i==0:
        div_sum+=i
if div_sum==n:
    print("is perfect number")
else:
    print("not perfect")      

# armstrong number
# palindrome
rev=0
p=n
while p>0:
    r=n%10
    rev=rev*10+r
    p//=10
if rev==p:
    print("palin")
else:
    print( "not palin")
