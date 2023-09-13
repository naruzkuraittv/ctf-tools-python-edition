from urllib.parse import unquote
import configparser
import os
import base64
import re

# Initialize global variable
boarder_style = 0

# Boarder styles dictionary
boarder_styles = {
    0: "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
    1: "__________________________________________________________________",
    2: "------------------------------------------------------------------",
    3: "<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
}

# Function to check and create config file (i cant be botehred to fix it so its called check and create config file () ;-; )
def check_and_create_config():
    global boarder_style
    print("Checking and creating config...")
    config = configparser.ConfigParser()
    config_file = 'NaruZKurai.encoder.config.txt'
    
    if os.path.exists(config_file):
        print("Config file exists. Reading...")
        config.read(config_file)
        if 'DEFAULT' in config and 'boarder_style' in config['DEFAULT']:
            boarder_style = int(config['DEFAULT']['boarder_style'])
            print(f"Boarder style set to {boarder_style}")
        else:
            print("Invalid config. Deleting...\n restarting config creator")
            os.remove(config_file)
            check_and_create_config()
    else:
        print("Config file does not exist. Creating...")
        config['DEFAULT'] = {'boarder_style': '0'}
        with open(config_file, 'w') as configfile:
            config.write(configfile)
        boarder_style = 0
        print("Config file created.")


def print_boarder(boarder_style):
    print(boarder_styles.get(boarder_style, "Invalid boarder style"))

def change_boarder():
    global boarder_style
    print_boarders()
    new_style = int(input("Which boarder do you like?: "))
    if new_style in boarder_styles.keys():
        boarder_style = new_style
        config = configparser.ConfigParser()
        config.read('NaruZKurai.encoder.config.txt')
        config['DEFAULT']['boarder_style'] = str(new_style)
        with open('NaruZKurai.encoder.config.txt', 'w') as configfile:
            config.write(configfile)
        print("Boarder style updated.")
    else:
        print("Invalid choice.")

# Function to preview all boarders
def print_boarders():
    for key, value in boarder_styles.items():
        print(f"{key}: {value}")


def hex_to_decimal_and_ascii():
    while True:
        print_boarder(boarder_style)
        hex_string = input("> (z)  go back to the menu \n> all hex numbers start with Ox and have numbers next to them\n> ex.0x70 0x69 0x63 0x6\n> Enter the hex string: ").strip()
        if hex_string.lower() == 'z':
            break
        
        hex_values = hex_string.split(" ")
        decimal_output = []
        ascii_output = []
        
        for hex_value in hex_values:
            try:
                decimal_value = int(hex_value, 16)
                decimal_output.append(str(decimal_value))
                
                if 0 <= decimal_value <= 1114111:  # Check if within Unicode range
                    ascii_char = chr(decimal_value)
                    ascii_output.append(ascii_char)
                else:
                    print("hex is out of ascii range (1114111), ")
                    ascii_output.append(f"[{decimal_value}]")  # Print the decimal value as a string
            except ValueError:
                print("Invalid hex value:", hex_value)
        print_boarder(boarder_style)
        print("Decimal Output:", " ".join(decimal_output))
        print_boarder(boarder_style) 
        print("ASCII Output:", "".join(ascii_output))


def decimal_to_hex():
    print_boarder(boarder_style)
    decimal_value = input("> (z)  go back to the menu\n> Enter the decimal value: ")
    if decimal_value.lower() == 'z':
        return
    try:
        hex_value = hex(int(decimal_value))
        print_boarder(boarder_style)
        print(f"Hex Output: {hex_value}")
    except ValueError:
        print_boarder(boarder_style)
        print("Decimal and Hex conversion failure.")
        print("Attempting ASCII to Hex conversion...")
        hex_value = " ".join(hex(ord(char)) for char in decimal_value)
        print("Hex:", hex_value)


def ascii_to_hex():
    while True:
        print_boarder(boarder_style)
        ascii_text = input("> (z)  go back to the menu \n> Enter the ASCII text: ")
        if ascii_text.lower() == 'z':
            break
        hex_value = " ".join(hex(ord(char)) for char in ascii_text)
        print("Hex:", hex_value)

def decode_url():
    while True:
        print_boarder(boarder_style)
        encoded_url = input("> (z)  go back to the menu \n> Enter the encoded URL: ").strip()
        if encoded_url.lower() == 'z':
            break
        decoded_url = unquote(encoded_url)
        print_boarder(boarder_style)
        print(f"Decoded URL: {decoded_url}")

#untested for bugs atm
def base64_to_ascii():
    while True:
        print_boarder(boarder_style)
        base64_string = input("> (z) go back to the menu \n> Enter the base64 string: ").strip()
        if base64_string.lower() == 'z':
            break
        try:
            decoded_string = base64.b64decode(base64_string).decode()
            print(f"Decoded ASCII: {decoded_string}")
        except:
            print("Invalid base64 string.")
#untested for bugs atm
def base32_to_ascii():
    while True:
        print_boarder(boarder_style)
        base32_string = input("> (z) go back to the menu \n> Enter the base32 string: ").strip()
        if base32_string.lower() == 'z':
            break
        try:
            decoded_string = base64.b32decode(base32_string).decode()
            print(f"Decoded ASCII: {decoded_string}")
        except:
            print("Invalid base32 string.")
#untested for edge case scenarios atm

def hex_stripper():
    stripped_hex_numbers = {}  # Temporary dictionary to store hex numbers
    counter = 1  # Counter to track dictionary entries
    
    while True:
        input_text = input("> (z) go back to the menu \n> (t) show all stored hex numbers \n> (clear) clear the stored hex numbers \n> Paste the text containing hex numbers: ").strip()
        
        if input_text.lower() == 'z':
            break
        elif input_text.lower() == 't':
            print("Stored Hex Numbers:", ' '.join([value for key, value in stripped_hex_numbers.items()]))
        elif input_text.lower() == 'clear':
            stripped_hex_numbers.clear()
            print("Cleared stored hex numbers.")
        else:
            hex_numbers = re.findall(r'0x[0-9A-Fa-f]+', input_text)
            hex_output = " ".join(hex_numbers)
            
            # Only add to dictionary if hex_output is not empty
            if hex_output:
                stripped_hex_numbers[counter] = hex_output  # Add to the dictionary
                counter += 1  # Increment counter for next entry
                
            print(f"Extracted Hex Numbers: {hex_output if hex_output else 'None'}")


# Don't forget to include or import your `print_boarder()` function and `boarder_style` variable as well.


def main():
    global boarder_style
    check_and_create_config()
    
    
    while True:
        print_boarder(boarder_style)
        print("Conversion Options:")
        print("(1) Decimal to Hex")
        print("(2) Hex to Decimal and ASCII")
        print("(3) ASCII to Hex")
        print("(4) Decode URL")
        print("(5) Change Boarders")
        print("(6) Base64 to ASCII nfs")
        print("(7) Base32 to ASCII nfs")
        print("(8) hex stripper")
        print("(9) Exit")
        print_boarder(boarder_style)
        choice = input("Enter your choice: ")
        
        if choice == '1':
            decimal_to_hex()
        
        elif choice == '2':
            hex_to_decimal_and_ascii()
        
        elif choice == '3':
            ascii_to_hex()
        
        elif choice == '4':
            decode_url()
        
        elif choice == '5':
            change_boarder()
            
        elif choice == '6':
            base64_to_ascii()
        
        elif choice == '7':
            base32_to_ascii()
            
        elif choice == '7':
            base32_to_ascii()
            
        elif choice == '8':
            hex_stripper()
            
        elif choice == '9':
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
