from utils import permute, shift_left
from permutation import PC1, PC2, SHIFT

def generate_keys(key64):

    round_keys = []

    # Step 1: Apply PC1
    key56 = permute(key64, PC1)

    # Step 2: Split into Left and Right
    left = key56[:28]
    right = key56[28:]

    # Step 3: Generate 16 round keys
    for i in range(16):

        # Left circular shifts
        left = shift_left(left, SHIFT[i])
        right = shift_left(right, SHIFT[i])

        # Combine healves
        combined = left + right

        #Apply PC2 to get 48-bit round key
        
        round_key = permute(combined, PC2)
        round_keys.append(round_key)

    return round_keys