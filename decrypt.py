alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("type 'encode' to encrypt, and 'decode' to decrypt ")
text = input("type your message: \n").lower()
shift = int(input("Type the shift number: "))


def decrypt(original_text, shift_amount):
    results = ""
    for i in original_text:
        num_shift= alphabet.index(i) - shift_amount
        results += alphabet[num_shift]
    print(f"the decrypted word is {results} ")

decrypt(original_text= "apple", shift_amount=2)