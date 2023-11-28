import random
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair():
    # Step 1: Choose two large prime numbers, p and q
    p = random_prime()
    q = random_prime()

    # Step 2: Compute n (the modulus), n = p * q
    n = p * q

    # Step 3: Compute the totient of n, totient(n) = (p-1) * (q-1)
    totient_n = (p - 1) * (q - 1)

    # Step 4: Choose e (public exponent) such that 1 < e < totient(n) and gcd(e, totient(n)) = 1
    e = random.randrange(2, totient_n)
    while gcd(e, totient_n) != 1:
        e = random.randrange(2, totient_n)

    # Step 5: Compute d (private exponent) such that d * e ≡ 1 (mod totient(n))
    d = mod_inverse(e, totient_n)

    return ((n, e), (n, d))

def random_prime():
    while True:
        num = random.randint(2**15, 2**16)
        if is_prime(num):
            return num

def encrypt(message, public_key):
    n, e = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    n, d = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return "".join(decrypted_message)

def main():
    message = input("Enter the message to be encrypted: ")

    public_key, private_key = generate_keypair()

    encrypted_message = encrypt(message, public_key)
    decrypted_message = decrypt(encrypted_message, private_key)

    print(f"Original message: {message}")
    print(f"Public key: {public_key}")
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")

if __name__ == "__main__":
    main()
