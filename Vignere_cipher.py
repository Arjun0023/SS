def generate_key(message, key):
    key = list(key)
    if len(message) == len(key):
        return key
    else:
        for i in range(len(message) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def vigenere_encrypt(message, key):
    encrypted_text = ""
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            # Shift value for the current character
            shift = ord(key[i].upper()) - 65
            if char.isupper():
                encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
            else:
                encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    key = generate_key(plaintext, key)
    encrypted_text = vigenere_encrypt(plaintext, key)

    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
