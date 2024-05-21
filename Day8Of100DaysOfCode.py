# Making Caesar's cipher.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
  encrypted_text = ""
  for char in text:
    if char in alphabet:
      index = alphabet.index(char)
      new_index = (index + shift) % 26
      encrypted_text += alphabet[new_index]
      
    else:
      encrypted_text += char
  print(f"The encoded text is {encrypted_text}")
  
def decode(text, shift):
    plaintext = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
        else:
            plaintext += char
    print(f"The decoded text is {plaintext}")
        

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


if direction == "encode":
  encrypt(text, shift)
if direction == "decode":
    decode(text, shift)