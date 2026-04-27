import math

def is_prime(n):
    # Corner cases: numbers <= 1 are not prime
    if n <= 1:
        return False
    # 2 is the only even prime
    if n == 2:
        return True
    # Eliminate all other even numbers immediately
    if n % 2 == 0:
        return False
    
    # Check for factors from 3 up to sqrt(n), skipping even numbers
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
            
    return True

# Read the number of test cases
t = int(input())
for _ in range(t):
    num = int(input())
    if is_prime(num):
        print("Prime")
    else:
        print("Not prime")
