# 0tn day =0 couple
# ist month =1 
#2nd m=2 
# 3=3
# 4th=5
# basically fibonacci
def fibonacci(num):
    if num==0:
        return 1;
    elif num==1:
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
print(fibonacci(10)) 
print(fibonacci(12))
print(fibonacci(24))
print(fibonacci(36))   