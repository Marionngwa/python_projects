alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
direction = input("type 'encode' to encrypt, and 'decode' to decrypt ")
text = input("type your message: \n").lower()
shift = int(input("Type the shift number: "))


def encrypt(txt, shift_amount):
    results = ""
    for i in txt:
        shift_base=alphabet.index(i) + shift_amount
        #results +=alphabet[shift_base]

        shift_base = shift_base % len(alphabet)
        results +=alphabet[shift_base]

    print(f"the encoded word is: {results}")
    

encrypt(txt=text, shift_amount = shift)