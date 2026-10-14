# Import and print the logo from art.py when the program starts.
from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        # What happens if the user enters a number/symbol/space?
        if letter not in alphabet:
            output_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


# restart the cipher program
should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction not in ("encode", "decode"):
        print("Incorrect choice. Terminating program.")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    rerun = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if rerun not in ("yes", "no"):
        print("Incorrect choice. Terminating program.")
        break
    elif rerun == "no":
        should_continue = False
        print("Goodbye")



