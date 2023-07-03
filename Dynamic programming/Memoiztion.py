### memoized version for nth Fibonacci number
import time
#initialize nill values in look up table
lookup = [0]*50
#function for fibonacci series

def fib(n):
    if(lookup[n]==0):
        if(n<=1):
            lookup[n]=n
        else:
            lookup[n]=fib(n-1)+fib(n-2)
    return lookup[n]        

s1 = time.time()
print(fib(10))
time_taken = time.time() - s1 
print('Time: ',time_taken)





