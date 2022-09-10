import random as rd

def isPrime(n):
    pass

def gcd(a,b):
    # euclidean's algorithm for finding gcd.
    if a == 0 or b == 0:
        # gcd(0, 3) = 3, gcd(3, 0) = 3. Return whichever is the max
        return max(a, b)
    return gcd(b, a % b)

def lcm(a,b):
    pass

# Generates public key exponent
def pubkExp(k):
    pass

# Generate private key exponent
def prikExp(x, y):
    pass

# Returns the hash of a string message. Sum of its ascii characters.
def hash(s):
    sum = 0
    for letter in s:
        sum += ord(letter)
    return sum
