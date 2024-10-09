import struct
def hashing(input:str)->any:
    # converting string to equivalent binary value
    res = ''.join(format(ord(i), '08b') for i in input)

    # adding padding, total size =  (512*i - 64)
    padded =res
    padded+='1'
    i = 1
    while len(padded) % 512 != 448:
        padded += '0'

    # we add the original message length (in bits) as a 64-bit integer
    sizeInBit = format(len(res), '064b')
    padded += sizeInBit


    # initialize four 32-bit buffers initialized to specific contsants

    A = 0x67452301; B= 0xEFCDAB89; C = 0x98BADCFE; D=0x10325476
    return len(padded)



print(hashing('abc'))

def F(x,y,z):
    return (x & y) | (~x & z)

def G(x,y,z):
    return (x & z) | (y & ~z)

def H(x, y, z):
    return  x ^ y ^ z

def I(x, y, z):
    return y ^ (x | ~z)





