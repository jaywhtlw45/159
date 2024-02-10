# This program provides an example of the RSA encryption algorithm

# First, determine all values for p,q,n,z,d,e
# 1. Choose two large prime numbers  p & q
#       If numbers are too large there is more computation required
#       If numbers are too small then the algorithm is less secure
# 2. n=p*q, z=(p-1)(q-1)
# 3. choose e (less than n) such that e has no common factor except 1 with z
# 4. find d such that ed-1 is divisibly by z

# Encryption (e,n):
# m->message, c->ciphertext
# c = (m^e)modn

# Decryption (d,n):
# m = (c^d)modn

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_pq():
    print("Both p and q must be prime, and p*q must be greater than 122")
    while True:
        p = int(input("Enter a prime value for p: "))
        q = int(input("Enter a prime value for q: "))

        if is_prime(p) and is_prime(q) and (p * q) > 122:
            return p, q
        else:
            print("Both p and q must be prime, and p*q must be greater than 122")

def get_nz(p, q):
    return p*q, (p-1)*(q-1)    

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def are_coprime(a, b):
    return gcd(a, b) == 1

def get_e(n, z):
    for e in range(2, z):
        if are_coprime(e, n) and are_coprime(e, z):
            return e
        
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = extended_gcd(b % a, a)
        return g, y - (b // a) * x, x
    
def mod_inverse(e, z):
    g, x, _ = extended_gcd(e, z)
    if g != 1:
        raise ValueError("The modular inverse does not exist")
    else:
        return x % z
    
# find d, such that e*d-1 is divisible by z       
def get_d(e, z):
    return mod_inverse(e, z)

def encrypt_message(ascii_values, e, n):
    return [pow(value, e, n) for value in ascii_values]

# def encrypt_message(ascii_values, e, n):
#     # return (pow(ascii_values, e, n))
#     ciphertext = [pow(value, e, n) for value in ascii_values]
#     return ciphertext

def decrypt_message(ciphertext, d, n):
    # return pow(ciphertext, d, n)
    return [pow(value, d, n) for value in ciphertext]

def is_all_letters(message):
    return all(char.isalpha() and (char.islower() or char.isupper()) for char in message)

def get_message():
    while True:
        message = input("Enter a message: ")
        if is_all_letters(message) & len(message) < 20:
            return message
        if (len(message) >= 20):
            print("Message is too long")
        print("Message must contain only letters")
  

def main():
    # Find values for p,q,n,z,e,d
    p, q= get_pq()
    n, z = get_nz(p,q)
    e = get_e(n, z)
    d = get_d(e, z)

    # message = "hello"
    # ascii_values = [ord(char) for char in message]
    # ciphertext = encrypt_message(ascii_values, e, n)
    # decrypted_text = decrypt_message(ciphertext, d, n)
    
    # print ("\np: ", p, "\nq: ", q, "\nn: ", n, "\nz: ", z)
    # print ("e: ", e, "\nd: ", d)
    # print ("\nMessage:                 ", message)
    # print ("ASCII Message:             ", ascii_values)
    # print ("Ciphertext:                ", ciphertext)
    # print ("Deciphered text:        ", decrypted_text)


    message = get_message()

    ascii_values = [ord(char) for char in message]
    cipher_ascii_text = encrypt_message(ascii_values, e , n)
    decrypted_ascii_text = decrypt_message(cipher_ascii_text, d, n)
    decrypted_message = ''.join(chr(value) for value in decrypted_ascii_text)

    print ("\np: ", p, "\nq: ", q, "\nn: ", n, "\nz: ", z)
    print ("e: ", e, "\nd: ", d)
    print ("\nMessage:            ", message)
    print ("ASCII values:       ", ascii_values)
    print ("Ciphertext:         ", cipher_ascii_text)
    print ("Decrypted text:     ", decrypted_ascii_text)
    print ("Deciphered message: ", decrypted_message)

main()

# Note chatgpt was used for get_d, mod_inverse, and extended_gcd funcitons.

    


