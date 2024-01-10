# Exponential power of a positive integer a^n(a, n≥0)  is defined as follows: 
# a^n={1 if  n=0 a*a*…*a if n>0 

def Exponential_power(a,n):
    for i in range(1,n):
        a=a*a
    return a
    
        
if __name__ == "__main__":
    print(Exponential_power(2,3))

# Basic OP: multiplication on line 8
# Worst case: other cases
# Count: T(n) = n
# Time complexity: O(n)
