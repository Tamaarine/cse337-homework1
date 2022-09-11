import random as rd
# import the mymath module here.
from mymath import mymath

class Rsa:
    # initialize to set p, q, and n.
    def __init__(self, p):
        # p is provided
        # n = p * q
        self.p = p
        self.q = p + 1000
        self.n = self.p * self.q

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
        
        d = mymath.prikExp(K, e)
        
        m = mymath.fast_mod(c, d, self.n)
        
        return m
