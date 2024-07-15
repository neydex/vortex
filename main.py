from colorama import Fore
import pyperclip
import base64

print(Fore.LIGHTBLUE_EX + "██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗")
print("██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝")
print("██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ ")
print("╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ ")
print(" ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗")
print("  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝")
print("")

action = input(Fore.LIGHTWHITE_EX + "Do you want to encode or decode?: " + Fore.LIGHTBLUE_EX)


if action == "encode":
    base = input(Fore.LIGHTWHITE_EX + "What encoding should be used (base85, base64, base32, base16)?: " + Fore.LIGHTBLUE_EX)
    string = input(Fore.LIGHTWHITE_EX + "Your text to encode: " + Fore.LIGHTBLUE_EX)
    string_bytes = string.encode("ascii")

    if base == "base64":
        base64_bytes = base64.b64encode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        print("Your encoded text:", Fore.LIGHTBLUE_EX + f"{base64_string}")
        pyperclip.copy(base64_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base32":
        base32_bytes = base64.b32encode(string_bytes)
        base32_string = base32_bytes.decode("ascii")
        print("Your encoded text:", Fore.LIGHTBLUE_EX + f"{base32_string}")
        pyperclip.copy(base32_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base16":
        base16_bytes = base64.b16encode(string_bytes)
        base16_string = base16_bytes.decode("ascii")
        print("Your encoded text:", Fore.LIGHTBLUE_EX + f"{base16_string}")
        pyperclip.copy(base16_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base85":
        base85_bytes = base64.b85encode(string_bytes)
        base85_string = base85_bytes.decode("ascii")
        print("Your encoded text:", Fore.LIGHTBLUE_EX + f"{base85_string}")
        pyperclip.copy(base85_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")

elif action == "decode":
    base = input(Fore.LIGHTWHITE_EX + "What decoding should be used (base64, base32, base16)?: " + Fore.LIGHTBLUE_EX)
    string = input(Fore.LIGHTWHITE_EX + "Your text to decode: " + Fore.LIGHTBLUE_EX)
    string_bytes = string.encode("ascii")

    if base == "base64":
        base64_bytes = base64.b64decode(string_bytes)
        base64_string = base64_bytes.decode("ascii")
        print("Your decoded text:", Fore.LIGHTBLUE_EX + f"{base64_string}")
        pyperclip.copy(base64_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base32":
        base32_bytes = base64.b32decode(string_bytes)
        base32_string = base32_bytes.decode("ascii")
        print("Your decoded text:", Fore.LIGHTBLUE_EX + f"{base32_string}")
        pyperclip.copy(base32_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base16":
        base16_bytes = base64.b16decode(string_bytes)
        base16_string = base16_bytes.decode("ascii")
        print("Your decoded text:", Fore.LIGHTBLUE_EX + f"{base16_string}")
        pyperclip.copy(base16_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    elif base == "base85":
        base85_bytes = base64.b85decode(string_bytes)
        base85_string = base85_bytes.decode("ascii")
        print("Your decoded text:", Fore.LIGHTBLUE_EX + f"{base85_string}")
        pyperclip.copy(base85_string)
        print(Fore.RESET + "Copied to clipboard")
        print("")
        input("Press enter to close.")
    else:
        print(Fore.RED + "Invalid encoding type. Please choose base64, base32, or base16."), input(Fore.RESET + "Press enter to close.")
else:
    print(Fore.RED + "Invalid action. Please choose encode or decode."), input(Fore.RESET + "Press enter to close.")

