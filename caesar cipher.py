alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    encrypt_message = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position + shift
        if new_position > 25:
            new_position = new_position-26
        new_letter = alphabet[new_position]
        encrypt_message += new_letter
    print("The encoded text is",encrypt_message)

def decrypt(text, shift):
    decrypt_message = ""
    for i in text:
        position = alphabet.index(i)
        new_position = position - shift
        new_letter = alphabet[new_position]
        decrypt_message += new_letter
    print("The decoded text is",decrypt_message)

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == "encode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text, shift)
        choice=input("Want to try again? yes or no? ")
        if choice=="yes":
            continue
        else:
            break
    elif direction == "decode":
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text, shift)
        choice=input("Want to try again? yes or no? ")
        if choice=="yes":
            continue
        else:
            break
    else:
        print("Please enter the right option")