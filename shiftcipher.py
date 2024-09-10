# PROGRAM DEKRIPSI - ENKRIPSI GERALD -140810220014
def encrypt(text, shift):
    result = ""

   
    for i in range(len(text)):
        char = text[i]

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        
        else:
            result += char

    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

text = input("Masukkan teks yang akan dienkripsi: ")
shift = int(input("Masukkan nilai kunci: "))

encrypted_text = encrypt(text, shift)
print(f"Teks terenkripsi: {encrypted_text}")

decrypted_text = decrypt(encrypted_text, shift)
print(f"Teks terdekripsi: {decrypted_text}")
