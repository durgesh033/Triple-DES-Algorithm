# ui.py

import tkinter as tk
from tkinter import messagebox
import pyperclip

from utils import (
    string_to_bitlist,
    bitlist_to_string,
    bitlist_to_hex,
    hex_to_bitlist
)

from triple_des import (
    triple_des_encryption,
    triple_des_decryption
)


# WINDOW 

root = tk.Tk()

root.title("Triple DES Encryption System")

root.geometry("1920x1080")

root.config(bg="#0F172A")

root.resizable(False, False)


# COLORS

BG_COLOR = "#0F172A"
CARD_COLOR = "#1E293B"
TEXT_COLOR = "#F8FAFC"
ENTRY_BG = "#334155"
BUTTON_COLOR = "#3B82F6"
BUTTON_HOVER = "#2563EB"


# MAIN FRAME

main_frame = tk.Frame(
    root,
    bg=CARD_COLOR,
    padx=30,
    pady=30
)

main_frame.place(relx=0.5, rely=0.5, anchor="center")


#TITLE

title = tk.Label(
    main_frame,
    text="TRIPLE DES ENCRYPTION SYSTEM",
    font=("Segoe UI", 24, "bold"),
    fg=TEXT_COLOR,
    bg=CARD_COLOR
)

title.pack(pady=(0, 25))


# INPUT FUNCTION

def create_input(label_text, hide=False):

    # Container Frame
    frame = tk.Frame(
        main_frame,
        bg=CARD_COLOR
    )

    frame.pack(fill="x", pady=10)

    # Label
    label = tk.Label(
        frame,
        text=label_text,
        font=("Segoe UI", 11, "bold"),
        fg=TEXT_COLOR,
        bg=CARD_COLOR
    )

    label.pack(anchor="w", pady=(0, 5))

    # Entry Box
    entry = tk.Entry(
        frame,
        width=40,
        font=("Consolas", 12),
        bg=ENTRY_BG,
        fg="white",
        insertbackground="white",
        relief="flat",
        bd=0
    )

    if hide:
        entry.config(show="•")

    entry.pack(ipady=10, fill="x")

    return entry


# INPUTS

plaintext_entry = create_input(
    "Plaintext (8 Characters)"
)

key1_entry = create_input(
    "Key 1",
    True
)

key2_entry = create_input(
    "Key 2",
    True
)

key3_entry = create_input(
    "Key 3",
    True
)


# OUTPUT BOX

output_label = tk.Label(
    main_frame,
    text="Output",
    font=("Segoe UI", 12, "bold"),
    fg=TEXT_COLOR,
    bg=CARD_COLOR
)

output_label.pack(anchor="w", pady=(20, 5))


output_box = tk.Text(
    main_frame,
    height=10,
    width=65,
    font=("Consolas", 11),
    bg="#020617",
    fg="#38BDF8",
    relief="flat",
    padx=15,
    pady=15
)

output_box.pack()


# GLOBAL CIPHER

cipher_hex = ""


# ENCRYPT FUNCTION

def encrypt_text():

    global cipher_hex

    try:

        plaintext = plaintext_entry.get().strip()

        key1 = key1_entry.get().strip()
        key2 = key2_entry.get().strip()
        key3 = key3_entry.get().strip()

        # Validation
        if (
            len(plaintext) != 8 or
            len(key1) != 8 or
            len(key2) != 8 or
            len(key3) != 8
        ):

            messagebox.showerror(
                "Error",
                "All inputs must be exactly 8 characters."
            )

            return

        # Convert plaintext to bits
        plain_bits = string_to_bitlist(plaintext)

        # Convert keys to bits
        k1_bits = string_to_bitlist(key1)
        k2_bits = string_to_bitlist(key2)
        k3_bits = string_to_bitlist(key3)

        # Triple DES Encryption
        cipher_bits = triple_des_encryption(
            plain_bits,
            k1_bits,
            k2_bits,
            k3_bits
        )

        # Convert encrypted bits to HEX
        cipher_hex = bitlist_to_hex(cipher_bits)

        # Clear Output Box
        output_box.delete("1.0", tk.END)

        # Show Results
        output_box.insert(
            tk.END,
            f"ORIGINAL TEXT\n"
            f"--------------------------\n"
            f"{plaintext}\n\n"
        )

        output_box.insert(
            tk.END,
            f"ENCRYPTED TEXT\n"
            f"--------------------------\n"
            f"{cipher_hex}"
        )

    except Exception as e:

        messagebox.showerror(
            "Encryption Error",
            str(e)
        )


# DECRYPT FUNCTION

def decrypt_text():

    global cipher_hex

    if cipher_hex == "":

        messagebox.showerror(
            "Error",
            "No ciphertext available."
        )

        return

    key1 = key1_entry.get()
    key2 = key2_entry.get()
    key3 = key3_entry.get()

    cipher_bits = hex_to_bitlist(cipher_hex)

    k1_bits = string_to_bitlist(key1)
    k2_bits = string_to_bitlist(key2)
    k3_bits = string_to_bitlist(key3)

    decrypted_bits = triple_des_decryption(
        cipher_bits,
        k1_bits,
        k2_bits,
        k3_bits
    )

    decrypted_text = bitlist_to_string(
        decrypted_bits
    )

    output_box.insert(
        tk.END,
        f"\n\nDECRYPTED TEXT\n"
        f"-------------------------\n"
        f"{decrypted_text}"
    )


# COPY FUNCTION

def copy_ciphertext():

    global cipher_hex

    if cipher_hex == "":

        messagebox.showerror(
            "Error",
            "No ciphertext found."
        )

        return

    pyperclip.copy(cipher_hex)

    messagebox.showinfo(
        "Copied",
        "Ciphertext copied successfully."
    )


# BUTTON STYLE

def create_button(text, command):

    btn = tk.Button(
        button_frame,
        text=text,
        command=command,
        width=18,
        height=2,
        font=("Segoe UI", 10, "bold"),
        bg=BUTTON_COLOR,
        fg="white",
        activebackground=BUTTON_HOVER,
        activeforeground="white",
        relief="flat",
        cursor="hand2"
    )

    return btn


# BUTTON FRAME 

button_frame = tk.Frame(
    main_frame,
    bg=CARD_COLOR
)

button_frame.pack(pady=25)


encrypt_btn = create_button(
    "Encrypt",
    encrypt_text
)

encrypt_btn.grid(row=0, column=0, padx=10)


decrypt_btn = create_button(
    "Decrypt",
    decrypt_text
)

decrypt_btn.grid(row=0, column=1, padx=10)


copy_btn = create_button(
    "Copy Ciphertext",
    copy_ciphertext
)

copy_btn.grid(row=0, column=2, padx=10)


# RUN APP

root.mainloop()