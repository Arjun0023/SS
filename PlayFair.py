def generate_playfair_matrix(key):
    key = key.upper().replace("J", "I")
    matrix = [['' for _ in range(5)] for _ in range(5)]
    chars = set()

    k = 0
    for i in range(5):
        for j in range(5):
            if k < len(key):
                matrix[i][j] = key[k]
                chars.add(key[k])
                k += 1
            else:
                for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
                    if ch not in chars:
                        matrix[i][j] = ch
                        chars.add(ch)
                        break

    return matrix

def find_position(matrix, char):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, key):
    matrix = generate_playfair_matrix(key)
    plaintext = plaintext.upper().replace("J", "I")
    ciphertext = ""

    i = 0
    while i < len(plaintext):
        char1 = plaintext[i]
        char2 = plaintext[i + 1] if i + 1 < len(plaintext) else 'X'

        row1, col1 = find_position(matrix, char1)
        row2, col2 = find_position(matrix, char2)

        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]

        i += 2

    return ciphertext

def main():
    plaintext = input("Enter the plaintext: ")
    key = input("Enter the key: ")

    encrypted_text = playfair_encrypt(plaintext, key)

    print(f"Plaintext: {plaintext}")
    print(f"Encrypted text: {encrypted_text}")

if __name__ == "__main__":
    main()
