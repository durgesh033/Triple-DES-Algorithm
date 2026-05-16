from key_generation import generate_keys
from des_core import des_encrypt, des_decrypt

def triple_des_encryption(plain_biits, key1_bits, key2_bits, key3_bits):
    key1 = generate_keys(key1_bits)
    key2 = generate_keys(key2_bits)
    key3 = generate_keys(key3_bits)

    des1 = des_encrypt(plain_biits, key1)
    des2 = des_encrypt(des1, key2)
    des3 = des_encrypt(des2, key3)

    return des3

def triple_des_decryption(cipher_bits, key1_bits, key2_bits, key3_bits):
    key1 = generate_keys(key1_bits)
    key2 = generate_keys(key2_bits)
    key3 = generate_keys(key3_bits)

    desd1 = des_decrypt(cipher_bits, key3)
    desd2 = des_decrypt(desd1, key2)
    desd3 = des_decrypt(desd2, key1)

    return desd3