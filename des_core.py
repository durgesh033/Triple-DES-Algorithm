from utils import permute, xor
from permutation import IP, FP, E, P
from sbox import S_BOXES

# S-box Substitutions

def sbox_substitution(bits):

    output = []

    #Process 8 blocks of 6 bits
    for i in range(8):
        block = bits[i * 6:(i + 1) * 6]

        #Row from first and last bit
        row = int(str(block[0]) + str(block[5]), 2)

        #Column from middle 4 bits
        col = int(''.join(map(str, block[1:5])), 2)

        #S-box lookup
        value = S_BOXES[i][row][col]

        #Convert to 4-bit binary
        binary = format(value, '04b')
        output.extend([int(bit) for bit in binary])

    return output

# One Feistal Round

def des_round(left, right, round_key):

    expanded_right = permute(right, E)
    xored = xor(expanded_right, round_key)
    substituted = sbox_substitution(xored)
    permuted = permute(substituted, P)
    new_right = xor(left, permuted)

    return right, new_right

# DES Encryption

def des_encrypt(block, round_keys):

    #Initial permutation
    block = permute(block, IP)

    left = block[:32]
    right = block[32:]

    for i in range(16):
        left, right = des_round(left, right, round_keys[i])

    combined = right + left
    cipher = permute(combined, FP)

    return cipher

# DES Decryption

def des_decrypt(block, round_keys):

    block = permute(block, IP)
    
    left = block[:32]
    right = block[32:]

    #Reverse round keys
    for i in range(15, -1, -1):
        left, right = des_round(left, right, round_keys[i])

    combined = right + left
    plain = permute(combined, FP)

    return plain