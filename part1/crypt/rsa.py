import random as rd
# import the mymath module here.
from mymath import mymath

class Rsa:
    # initialize to set p, q, and n.
    def __init__(self, X):
        # X is provided to generate p and q which are distinct prime between
        # [X, X + 1000]
        # n = p * q
        p = 1
        q = 1
        while not mymath.isPrime(p):
            p = rd.randint(X, X + 1000)
        while not mymath.isPrime(q) or p == q:
            q = rd.randint(X, X + 1000)
        self.p = p
        self.q = q
        self.n = p * q            

    # generates a cipher string for a message m
    def encrypt(self, m):
        '''
        message m, is hashed already
        
        Return both the cipher text, and the public key generated
        '''
        K = mymath.lcm(self.p - 1, self.q - 1)
        e = mymath.pubkExp(K) # Generate e, public key
        
        c = mymath.fast_mod(m, e, self.n)
        
        return c, e

    # decrypts a cipher string to get back original message
    def decrypt(self, c, e):
        '''
        c, is the ciphertext
        e, is the public key
        
        Decrypt the ciphertext using e and return the message
        that is decrypted
        '''
        K = mymath.lcm(self.p - 1, self.q - 1)
        
        d = mymath.prikExp(e, K)
        
        m = mymath.fast_mod(c, d, self.n)
        
        return m
