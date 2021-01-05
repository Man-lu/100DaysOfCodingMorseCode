from colorama import Fore
from data import morse_dict

continue_to_encode_or_decode = True

print(f"{Fore.MAGENTA}############## MORSE CODE | ENCODE AND DECODE MESSAGES ##############{Fore.MAGENTA}")


def encode_message():
    """"Encodes Normal Text, Numbers and Some Punctuation into Morse Code"""
    message = input(f"****** TYPE IN THE MESSAGE TO ENCODE :\n{Fore.RESET}")
    message = message.replace(" ", "|").upper()

    encoded_message = []
    for char in message:
        try:
            encoded_message.append(morse_dict[char])
        except KeyError:
            print(f"{Fore.LIGHTRED_EX}******I Cannot Recognize One or More of Your Letters: ******{Fore.RESET}")
        encoded_message.append(" ")

    print(f"{Fore.MAGENTA}******Your Encoded Message is as follows: ******{Fore.RESET}")
    print(f"{Fore.CYAN}<START> {Fore.RESET} {''.join(encoded_message)} {Fore.CYAN} <END>")


def decode_message():
    """"Decodes the Morse Code into a Normal Text"""
    message = input(f"****** TYPE IN THE MORSE CODE TO DECODE "
                    f"{Fore.RED}**USE 'SPACE' TO SEPARATE MORSE CODE REPRESENTING A LETTER AND '|' "
                    f"TO SEPARATE WORDS :\n{Fore.RESET}\n").split(" ")

    decoded_message = []
    for char in message:
        for key,value in morse_dict.items():
            if value == char:
                decoded_message.append(key)

    decoded_message = "".join(decoded_message).replace("|", " ").title()

    print(f"{Fore.MAGENTA}******Your Decoded Message is as follows: ******{Fore.RESET}")
    print(f"{Fore.CYAN}<START> {Fore.RESET} {decoded_message} {Fore.CYAN} <END>")


while continue_to_encode_or_decode:
    encode_decode = input(f"{Fore.LIGHTGREEN_EX}############## Type 'E' to Encode and 'D' to Decode"
                          f" and 'any key' to Quit ##############\n{Fore.RESET}").lower()
    if encode_decode == 'e':
        encode_message()
    elif encode_decode == 'd':
        decode_message()
    else:
        print(f"{Fore.RED}******You Have Quit Encoding or Decoding: ******{Fore.RESET}")
        continue_to_encode_or_decode = False
