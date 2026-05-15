from utils import string_to_bitlist, bitlist_to_string
from key_generation import generate_keys
from des_core import des_encrypt, des_decrypt

plaintext = "ABCDEFGH"
key = "12345678"

plain_bits = string_to_bitlist(plaintext)
key_bits = string_to_bitlist(key)

round_keys = generate_keys(key_bits)

cipher_bits = des_encrypt(
    plain_bits,
    round_keys
)

decrypted_bits = des_decrypt(
    cipher_bits,
    round_keys
)

print("Original:")
print(plaintext)

print("\nEncrypted Bits:")
print(cipher_bits)

print("\nDecrypted:")
print(bitlist_to_string(decrypted_bits))