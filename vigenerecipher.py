def vigenere_encrypt(plaintext, key):
    encrypted_text = []
    key_length = len(key)
    
    key_extended = (key * (len(plaintext) // key_length)) + key[:len(plaintext) % key_length]

    for p_char, k_char in zip(plaintext, key_extended):
        if p_char.isalpha(): 
            p_val = ord(p_char.upper()) - ord('A')
            k_val = ord(k_char.upper()) - ord('A')
            encrypted_char = chr((p_val + k_val) % 26 + ord('A'))
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(p_char)  

    return ''.join(encrypted_text)

def vigenere_decrypt(encrypted_text, key):
    decrypted_text = []
    key_length = len(key)
    
    
    key_extended = (key * (len(encrypted_text) // key_length)) + key[:len(encrypted_text) % key_length]

    for e_char, k_char in zip(encrypted_text, key_extended):
        if e_char.isalpha():  
            e_val = ord(e_char.upper()) - ord('A')
            k_val = ord(k_char.upper()) - ord('A')
            decrypted_char = chr((e_val - k_val + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(e_char)  

    return ''.join(decrypted_text)


plaintext = input("Masukkan plainteks: ")
key = input("Masukkan kunci: ")


encrypted = vigenere_encrypt(plaintext, key)
print(f"Teks terenkripsi: {encrypted}")


decrypted = vigenere_decrypt(encrypted, key)
print(f"Teks terdekripsi: {decrypted}")
