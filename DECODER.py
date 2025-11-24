def encoder_decoder():

    print("Encoder Decoder")

    user_message = input("Enter your message: ")
    user_key = input("Enter your key: ")

    output_message = ""

    for index, char in enumerate(user_message):

        current_key_char = user_key[index % len(user_key)]

        result = ord(char)^ord(current_key_char)

        output_message += chr(result)

    print(output_message)

if __name__ == "__main__":
    encoder_decoder()
