import hashlib

def md5_hash(text):
    # Create an MD5 hash object
    md5 = hashlib.md5()

    # Update the hash object with the bytes-like object of the input text
    md5.update(text.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    hashed_text = md5.hexdigest()

    return hashed_text

# Example usage
if __name__ == "__main__":
    # Input text to be hashed
    input_text = "Hello, This is Arjun"

    # Get the MD5 hash of the input text
    hashed_text = md5_hash(input_text)

    # Print the original text and its MD5 hash
    print(f"Original Text: {input_text}")
    print(f"MD5 Hash: {hashed_text}")
