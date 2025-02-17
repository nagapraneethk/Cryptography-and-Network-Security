import math

#Q.1: Generating RSA Keys
def generateKeys():
    p = 1031
    q = 1049

    n = p * q
    phi = (p - 1) * (q - 1)

#for e-- (e,phi)=>coprimes
    for x in range(2, phi):
        if math.gcd(x, phi) == 1:
            e=x
            break

#for d=> (e*d)%pi=1
    for x in range(2, phi):
        if (e * x) % phi == 1:
            d=x

    return e,d,n


#Q.2 : Encryption & Decryption of inp

def encrypt(inp, e, n):
    return pow(inp, e, n)

def decrypt(inp, d, n):
    return pow(inp, d, n)

def enc_dec():
    e,d,n=generateKeys()
    print(f"Keys generated:\ne: {e}\nd: {d}\nn: {n}\n")


    inp_num = 123
    encrypted_num = encrypt(inp_num, e, n)
    decrypted_num = decrypt(encrypted_num, d, n)
    print(f"Number: {inp_num}\nEncrypted: {encrypted_num} -> Decrypted: {decrypted_num}\n")

    char = 'P'
    ascii_val = ord(char)
    encrypted_char = encrypt(ascii_val, e, n)
    decrypted_char = chr(decrypt(encrypted_char, d, n))
    print(f"Alphabet: {char}\nEncrypted: {encrypted_char} -> Decrypted: {decrypted_char}\n")


if __name__ == "__main__":
    # e,d,n=generateKeys()
    # print(f"Keys generated:\ne: {e}\nd: {d}\nn: {n}")
    enc_dec()