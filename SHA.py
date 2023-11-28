import hashlib

def sha256_hash(text):
    # Create an SHA-256 hash object
    sha256 = hashlib.sha256()

    # Update the hash object with the bytes-like object of the input text
    sha256.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = sha256.hexdigest()

    return hashed_text

# Example usage
if __name__ == "__main__":
    # Input text to be hashed
    input_text = "Hello, World!"

    # Get the SHA-256 hash of the input text
    hashed_text = sha256_hash(input_text)

    # Print the original text and its SHA-256 hash
    print(f"Original Text: {input_text}")
    print(f"SHA-256 Hash: {hashed_text}")
