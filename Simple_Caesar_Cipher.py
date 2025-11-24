# Stephen Hernandez
#extra credit




def caesar_cipher():
    print("Caesar Cipher")
    choice = input("Encrypt or Decrypt (e/d): ")
    message = input ("Message : ")
    key = int(input("Key : "))

    new_message = ""



    for char in message:

        if char.isalpha():
            if char.isupper():
                start=ord('A')
            else:
                start=ord('a')

            if choice == "e":
                offset=(ord(char)-start+key)%26
            else:
                offset=(ord(char)-start-key)%26

            new_char = chr(start+offset)
            new_message += new_char

        else:
            new_message += char

    print("result:")
    print(new_message)


if __name__ == "__main__":
    caesar_cipher()
