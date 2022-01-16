alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encode(text, shift):
  encoded_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      if new_position > len(alphabet) - 1:
        new_position -= len(alphabet) - 1
      encoded_text += alphabet[new_position]      
    elif letter == " ":
      encoded_text += " "
  if letter not in alphabet:
    print("You've typed not only letters.")
    
  else :
    print(encoded_text)

def decode(text, shift):
  decoded_text = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position - shift
      if new_position < 0:
        new_position += len(alphabet) - 1
      decoded_text += alphabet[new_position]
    elif letter == " ":
      decoded_text += " "
  if letter not in alphabet:
    print("You've typed not only letters.")
    
  print(decoded_text)

def main(direction):
  if direction == "e":
    encode(text, shift)
  elif direction== "d":
    decode(text, shift)
  else :
    print("Yo've typed invalid command.")

main(direction)