
#caeser cypher game 
def caeser(original_text, shift_amount, options):
    final_text = ""
    if options == "decode":
        shift_amount *= -1
        
    for i in original_text:

        if i not in alphabet:
            final_text +=i
        else:
            num_shift= alphabet.index(i) + shift_amount
            final_text+= alphabet[num_shift]
    print(f"the {options}d word is {final_text} ")

forward = True
while forward:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    direction = input("type 'encode' to encrypt, and 'decode' to decrypt ")
    text = input("type your message: \n").lower()
    shift_amount = int(input("Type the shift number: "))
    caeser(original_text=text, shift_amount=2, options=direction)

    go_again = input("Do you want to go again? type 'y' for yes and 'n' for no: ").lower()
    if go_again == "n":
        forward = False
        print("Thank you and goodbye")