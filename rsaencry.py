
######Enycrypt########

import math


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# p and q found by searching for twin primes.

p = 7667711
q = p + 2
n = p * q # '0x3578ffffffff'
e = 65537
plaintext = "Hi"
print plaintext
m = int(plaintext.encode("hex"), 16) # 18537
c = pow(m, e, n)

print c


####################Decrypt###################

fi = (p-1)*(q-1)
d = modinv(e, fi)
print ("%x" % pow(c, d, n)).decode("hex") # prints 'Hi'


#####Decrypt the message using the public key##################


e = 65537

# modulus = 0x3578ffffffff
# modulus = (sqrt(prefix) * 2^x)^2
# sqrt(prefix) * 2^x - 1 = p

prefix = 0x3578
sqrt_of_prefix = math.sqrt(prefix + 1)

# 4 sets of ff => 256^4 = 2^8^4 = 2^32 = (2^16)^2
# sqrt of modulus = sqrt(prefix) * sqrt(2^16)
sqrt_of_modulus = sqrt_of_prefix * 2**16
p, q = sqrt_of_modulus - 1, sqrt_of_modulus + 1
fi = (p-1)*(q-1)
d = int(modinv(e, fi))
print ("%x" % pow(c, d, n)).decode("hex") # Also prints 'Hi'

