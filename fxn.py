def is_even(num):
    """
    Check if a number is even or odd.
    input = any valid number;
    output=even/odd
    created by:'GOLDI SINGH'
    on 2026 july
        """
    if num%2==0 :
        return "even"
    else :
        return "odd"
    
for i in range(1,10) :
        print(is_even(i))
print(is_even.__doc__)     
    