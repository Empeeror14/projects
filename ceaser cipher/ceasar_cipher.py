
def ceasar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char  in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter =alphabet[new_position]
            end_text +=new_letter
        else:
            end_text += char
    print(f"The {cipher_direction}d text is {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from ceasar_cipher_art import logo
print(logo)
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    text = input("Type your message: \n ").lower()
    shift = int(input("Type your shift number: \n"))
    shift = shift % 26

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("Type 'yes' to go again or type 'no' to exit: \n")
    if result == "no":
        should_continue = False
        print("Goodbye")
        
# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)


