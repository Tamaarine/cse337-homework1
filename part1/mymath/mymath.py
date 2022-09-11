import random as rd

def isPrime(n):
    # To check if a number is prime
    # just loop through every integer from 2 to sqrt(n)
    # if it evenly divides it then it is not a prime.
    if n == 1:
        return False
    
    maxCheck = int(n ** 1/2)
    # Plus one to be safe
    for i in range(2, maxCheck + 1):
        if n % i == 0:
            return False
    return True

def gcd(a,b):
    # euclidean's algorithm for finding gcd.
    if a == 0 or b == 0:
        # gcd(0, 3) = 3, gcd(3, 0) = 3. Return whichever is the max
        return max(a, b)
    return gcd(b, a % b)

def lcm(a,b):
    # To find least common multiple use gcd.
    # formula is just |a * b| / gcd(a, b)
    # Handle absolute value 
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    return int((a * b) / gcd(a, b))

# Generates public key exponent
def pubkExp(k):
    # Picking a value for e, which is an integer
    # 1 < e < k, such that e is a co-prime of k
    # gcd(e, k) == 1
    e = rd.randint(2, k - 1)
    
    while gcd(e, k) != 1:
        e = rd.randint(2, k - 1)
    return e
    
# Generate private key exponent
def prikExp(x, y):
    '''
    https://www.extendedeuclideanalgorithm.com/multiplicative_inverse.php
    
    yea, naw I'm not going to try to understand the math behind it
    
    just gonna go oonga ooga create table to find answer
    
    x - > e
    
    y -> K
    
    This function returns the modular multiplicative inverse if it exist.
    Otherwise return -1
    '''
    # If x < y then swap them otherwise keep them the same
    if x < y:
        x, y = y, x # Swap em because I used them in the context differently
        
    table = []
    first_row = [x, y, x // y, x % y, 0, 1, 0 - x // y * 1] # First row
    if first_row[3] == 0 and first_row[1] != 1:
        # There is no modular multiplicative inverse
        return -1
    elif first_row[3] == 0 and first_row[1] == 1:
        return first_row[5] % x
    
    table.append(first_row)
    i = 1 # Keep track of the current working row
    while True:
        prev_row = table[i - 1]
        
        n = prev_row[1]
        b = prev_row[3]
        q = n // b
        r = n % b
        t1 = prev_row[5]
        t2 = prev_row[6]
        t3 = t1 - q * t2
        
        row = [n, b, q, r, t1, t2, t3]
        table.append(row)
        i += 1
        
        if r == 0 and row[1] == 1:
            # Last row and is multiplicative inverse
            # Just do t2 % x is our answer
            return t2 % x
        elif r == 0:
            # Last row but column b isn't 1, no multiplicative inverse
            return -1
            

# Returns the hash of a string message. Sum of its ascii characters.
def hash(s):
    sum = 0
    for letter in s:
        sum += ord(letter)
    return sum

def fast_mod(a, b, m):
    '''
    Doing fast exponentiation with large numbers
    to be memory efficient.
    a -> The base number
    b -> Exponent
    m -> The mod to take the a^b by
    '''
    # The way that fast exponentitation works is that
    # you basically check if the current base is even or odd
    # if it is odd, you just take odd one out and rest are even,
    # example, a^513 -> a * a^512. You store that result into extra
    # which will be used later.
    # Then the rest of the even number goes through the multiplication process
    # you update a to be a raised to the power by 2, so a * a, then take the mod.
    # After the if-statement you do rightshift of b to divide by 2.
    
    # 45 ** 101 mod 59
    # Store 45 mod 59 = 49 into extra.
    # 45 ** 100 mod 59. a is current 45.
    # 45 * 45 = 2025 mod 59. a = 19, b = 50
    # 19 * 19 = 361 mod 59. a = 7, b = 25
    # 7 * 7 = 49 mod 59. a = 49, b = 12 
    # 49 * 49 = 2401 mod 59. a = 41, b = 6
    # 41 * 41 = 1681 mod 59. a = 29, b = 3
    # 29 * 29 = 841 mod 59. a = 15, b = 1
    # so the result is (15 * 49) mod 59 = 27
    extra = 1
    while b > 1:
        if b % 2 == 1:
            extra = b % m
            b -= 1
        a = (a ** 2) % m
        # Bitshift by 1 to half it
        b = b >> 1
    return (a * extra) % m
    