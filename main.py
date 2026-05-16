from utils import string_to_bitlist, bitlist_to_string, bitlist_to_hex
from triple_des import triple_des_decryption, triple_des_encryption

print("TRIPLE DES ENCRYPTION")

plaintext = input("\n Enter 8-character plain text: ")
key1 = input("Enter Key 1 (8 characters): ")
key2 = input("Enter Key 2 (8 character): ")
key3 = input("Enter key 3 (8 characters): ")

if(
    len(plaintext) != 8 or
    len(key1) != 8 or
    len(key2) != 8 or
    len(key3) != 8 
):
    print("\n Error:")
    print("Plain text and key must be 8 characters")

    exit()

    #Encryption

plain_bits = string_to_bitlist(plaintext)

k1 = string_to_bitlist(key1)
k2 = string_to_bitlist(key2)
k3 = string_to_bitlist(key3)

cipher_bits = triple_des_encryption(plain_bits, k1, k2, k3)
cipher_text = bitlist_to_hex(cipher_bits)

#deccryption

decrypted_bits = triple_des_decryption(cipher_bits, k1, k2, k3)

decrypted_text = bitlist_to_string(decrypted_bits)

#Display Output

print("\n Original text")
print(plaintext)

print("Encrypted text")
print(cipher_text)

print("Decrypted text")
print(decrypted_text)



