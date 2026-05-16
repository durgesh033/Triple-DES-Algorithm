# permutation function

def permute(block, table):
    return [block[i - 1] for i in table]

# Left Circular Shift

def shift_left(bits, n):
    return bits[n:] + bits[:n]


# XOR Function
def xor(a, b):
    return [ i ^ j for i, j in zip(a ,b)]

#Convert String to Bit List
def string_to_bitlist(text):
    bit_list = []
    for char in text:

        #Convert character to 8-bit binary
        binary = format(ord(char), '08b')

        #Add bits to list
        bit_list.extend([int(bit) for bit in binary])

    return bit_list;

def bitlist_to_string(bits):

    text = ""

    #Process every 8 bits
    for i in range(0, len(bits), 8):
        byte = bits[i:i + 8]

        if (len(byte) < 8):
            continue

        #Convert bits to character
        binary = ''.join(map(str, byte))
        text += chr(int(binary, 2))

    return text

# Convert bit list to hexadecimal
def bitlist_to_hex(bits):

    binary_string = ''.join(map(str, bits))

    while(len(binary_string) % 4 != 0):
        binary_string = '0' + binary_string

    hex_string = hex(
        int(binary_string, 2)
    )[2:].upper()

    return hex_string


# Convert hexadecimal to bit list
def hex_to_bitlist(hex_string):

    # Convert each hex digit to 4-bit binary
    binary_string = ''.join(
        format(int(char, 16), '04b')
        for char in hex_string
    )

    return [int(bit) for bit in binary_string]