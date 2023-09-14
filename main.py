from urllib.parse import unquote, urlparse, parse_qs, urlencode, urlunparse
import configparser
import os
import base64
import re
import hashlib
import hmac
#YES I KNOW A BIG SCRIPT ISNT OPTIMAL later ill do start.py then itll do all the init stuff then ask then push u into the start menu its just a mess rn.
# Initialize global variable

class Border:
    def __init__(self):
        self.style = 0
        self.styles = {
            0: "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-",
            1: "__________________________________________________________________",
            2: "------------------------------------------------------------------",
            3: "<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
        }
        self.config_file = 'NaruZKurai.encoder.config.txt'

    def print(self):
        print(self.styles.get(self.style, "Invalid border style"))

    def change(self):
        for key, value in self.styles.items():
            print(f"{key}: {value}")
        new_style = input("Which border do you like?: ")
        if new_style in self.styles.keys():
            self.style = new_style
            print("border style updated.")
            self.make()  # Update the config file
        else:
            self.change()
            print("Invalid choice.")

    def check_if_exist(self):
        return os.path.exists(self.config_file)

    def make(self):
        config = configparser.ConfigParser()
        config['DEFAULT'] = {'border_style': str(self.style)}
        with open(self.config_file, 'w') as configfile:
            config.write(configfile)
        print("Config file created.")

    def delete(self):
        os.remove(self.config_file)
        print("Config file deleted.")

    def set(self):
        config = configparser.ConfigParser()
        config.read(self.config_file)
        if 'DEFAULT' in config and 'border_style' in config['DEFAULT']:
            self.style = int(config['DEFAULT']['border_style'])
            print(f"border style set to {self.style}")
        else:
            print("Invalid config. Deleting...")
            self.delete()
class Startup:
    def __init__(self, border):
        self.border = border

    def start(self):
        print("Checking and creating config...")
        if border.check_if_exist():
            print("Config file exists. Reading...")
            border.set()
        else:
            print("Config file does not exist. Creating...")
            border.make()


class Converter:
    def __init__(self, border_style):
        self.border_style = border_style

    def hex_to_decimal_and_ascii(self):
        while True:
            (self.border_style)
            hex_string = input("> (z)  go back to the menu \n> all hex numbers start with 0x and have numbers next to them\n> ex. 0x70 0x69 0x63 0x6\n> Enter the hex string: ").strip()
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
                        print("Hex is out of ASCII range (1114111).")
                        ascii_output.append(f"[{decimal_value}]")  # Print the decimal value as a string
                except ValueError:
                    print("Invalid hex value:", hex_value)
            border.print()
            print("Decimal Output:", " ".join(decimal_output))
            border.print() 
            print("ASCII Output:", "".join(ascii_output))

    def decimal_to_hex(self):
        border.print()
        decimal_value = input("> (z)  go back to the menu\n> Enter the decimal value: ")
        if decimal_value.lower() == 'z':
            return
        try:
            hex_value = hex(int(decimal_value))
            border.print()
            print(f"Hex Output: {hex_value}")
            border.print()
        except ValueError:
            border.print()
            print("Decimal and Hex conversion failure.")
            print("Attempting ASCII to Hex conversion...")
            hex_value = " ".join(hex(ord(char)) for char in decimal_value)
            print("Hex:", hex_value)
            border.print()

    def ascii_to_hex(self):
        while True:
            border.print()
            ascii_text = input("> (z)  go back to the menu \n> Enter the ASCII text: ")
            if ascii_text.lower() == 'z':
                break
            hex_value = " ".join(hex(ord(char)) for char in ascii_text)
            print("Hex:", hex_value)
            border.print()

    def decode_url(self):
        while True:
            border.print()
            encoded_url = input("> (z)  go back to the menu \n> Enter the encoded URL: ").strip()
            if encoded_url.lower() == 'z':
                break
            decoded_url = unquote(encoded_url)
            border.print()
            print(f"Decoded URL: {decoded_url}")
            border.print()

    def base64_to_ascii(self):
        while True:
            border.print()
            base64_string = input("> (z) go back to the menu \n> Enter the base64 string: ").strip()
            if base64_string.lower() == 'z':
                break
            try:
                decoded_string = base64.b64decode(base64_string).decode()
                print(f"Decoded ASCII: {decoded_string}")
                border.print()
            except:
                print("Invalid base64 string.")

    def base32_to_ascii(self):
        while True:
            border.print()
            base32_string = input("> (z) go back to the menu \n> Enter the base32 string: ").strip()
            if base32_string.lower() == 'z':
                break
            try:
                decoded_string = base64.b32decode(base32_string).decode()
                print(f"Decoded ASCII: {decoded_string}")
                border.print()
            except:
                print("Invalid base32 string.")
                border.print()



#hex stripper #untested for edge case scenarios atm
class Stripper:
    def __init__(self, style):
        self.style = style    
    def help():
        print("(help), this print function\n (tamper main menu) paste in a bunch of text and if there are any hex values that are 0xnumber itll steal them then spit them out when you click t\n (t) spits out the stored\m (clear) clears the table of all known hex values.")
        stripper.hex()
    def hex():
        stripped_hex_numbers = {}  # Temporary dictionary to store hex numbers
        counter = 1  # Counter to track dictionary entries
        while True:
            input_text = input("> (z) go back to the menu \n> (t) show all stored hex numbers \n> (clear) clear the stored hex numbers\n (help) help \n> Paste the text containing hex numbers: ").strip()
            
            if input_text.lower() == 'z':
                break
            elif input_text.lower() == 't':
                print("Stored Hex Numbers:", ' '.join([value for key, value in stripped_hex_numbers.items()]))
            elif input_text.lower() == 'clear':
                stripped_hex_numbers.clear()
                print("Cleared stored hex numbers.")
#need to add an elif function to save to file and an option to just search for number strings and turn that into 0xnumbers then allow quic convert to ascii
            else:
                hex_numbers = re.findall(r'0x[0-9A-Fa-f]+', input_text)
                hex_output = " ".join(hex_numbers)
                
                # Only add to dictionary if hex_output is not empty
                if hex_output:
                    stripped_hex_numbers[counter] = hex_output  # Add to the dictionary
                    counter += 1  # Increment counter for next entry
                border.print()
                print(f"Extracted Hex Numbers: {hex_output if hex_output else 'None'}")
#the tamperer was for something realy weird
class Tamperer:
    def __init__(self, border_style):
        self.border_style = border_style

    def extract_url_parameters(self, url):
        parsed_url = urlparse(url)
        params = parse_qs(parsed_url.query)
        return params
    def help():
        print("help, this menu\n paste in a url and itll try to extract the visible secret key and key pair from the url. then generate a mew url based on encoding alg\n its super basic")
        tamperer.start()
    def tamper_parameters(self, params, secret_key=None):
        tampered_params = params.copy()
        
        # This will either update the existing 'Key-Pair-Id' or add a new one
        tampered_params['Key-Pair-Id'] = ['NEW_KEY_PAIR_ID']

        if secret_key:
            tampered_params['Secret-Key'] = [hashlib.sha256(secret_key.encode()).hexdigest()]

        return tampered_params

    def generate_new_url(self, base_url, params):
        new_query = urlencode(params, doseq=True)
        new_url = urlunparse((base_url.scheme, base_url.netloc, base_url.path, base_url.params, new_query, base_url.fragment))
        return new_url

    def start(self):
        border.print()  
        url = input("What's the URL, bro? ")
        border.print()  
        if url == "help":
          self.help
        else:
            know_secret_key = qol.yesno("Do you know the secret key?", 'v')

        if know_secret_key == "yes":
            secret_key = input("Enter it: ")
            parsed_url = urlparse(url)
            params = self.extract_url_parameters(url)
            tampered_params = self.tamper_parameters(params, secret_key)
        elif know_secret_key == "no":
            parsed_url = urlparse(url)
            params = self.extract_url_parameters(url)
            tampered_params = self.tamper_parameters(params)
        else:
            print("Invalid choice for the secret key. Try again.")
            self.url_tamper()
            return

        border.print()
        print(f"Extracted Parameters: {params}")
        border.print()
        print(f"Tampered Parameters: {tampered_params}")
        border.print()
        new_url = self.generate_new_url(parsed_url, tampered_params)
        print(f"New URL: {new_url}")
        border.print()
        # Ask the user if they want to do more
        more_qm = qol.yesno("Do you want to do more?", 'v')
        if more_qm == "yes":
            self.start()  # Call the start method again
        else:
            return

class QoL:
    def __init__(self, style):
        self.style = style
    def yesno(self, prompt, format_type):
        while True:
            user_input = input(str(border.style)  + "\n" + prompt + " \n(1)yes  (2)no): ").strip().lower()
            if user_input in ['1', 'y', 'ye', 'yes']:
                if format_type in ["verbose", "v", "word", "w", None]:
                    return 'yes'
                elif format_type in ["n"]:
                    return 1
                elif format_type in ["tf"]:
                    return True
            elif user_input in ['2', 'n', 'no']:
                if format_type in ["verbose","v", "word", "w", None]:
                    return 'no'
                elif format_type in ["n"]:
                    return 2
                elif format_type in ["tf"]:
                    return False
            else:
                print("Error: Please type 'yes' or 'no'.")
class Menus:
    def __init__(self, border):
        self.border = border
    
    def start(self):
        while True:
            border.print()
            print("We have two modes:")
            print("(1) Converter Mode")
            print("(2) Tamper Mode")
            border.print()
            choice = input("Enter your choice: ")

            if choice == '1':
                self.converter()  # Call the converter menu
            elif choice == '2':
                # Implement tamper menu here if needed
                pass
            else:
                print("Invalid choice. Please select a valid option.")

    def converter(self):
        while True:
            border.print()
            print("Conversion Options:")
            print("(1, d2hex) Decimal to Hex")
            print("(2, h2da) Hex to Decimal and ASCII")
            print("(3, h2a) ASCII to Hex")
            print("(4, urld) Decode URL")
            print("(5, cb, change, border, change border) Change border")
            print("(6, b64) Base64 to ASCII nfs")
            print("(7, b32) Base32 to ASCII nfs")
            print("(8, hs) Hex Stripper")
            print("(9) Exit")
            print("(urltamper, restart, start menu, start,) extras")
            border.print()

            choice = input("Enter your choice: ")
            
            if choice in ['1', 'd2hex']:
                converter.decimal_to_hex()
            elif choice in ['2', 'h2da']:
                converter.hex_to_decimal_and_ascii()
            elif choice in ['3', 'a2h']:
                converter.ascii_to_hex()
            elif choice in ['4', 'urld']:
                converter.decode_url()  
            elif choice in ['5', 'change', 'border', 'change border']:
                border.change()
            elif choice in ['6', 'b64']:
                converter.base64_to_ascii() 
            elif choice in ['7', 'b32']:
                converter.base32_to_ascii()  
            elif choice in ['8', 'hs']:
                stripper.hex()  # Call the method from the stripper class (i just now realised after being up 21hrs that the word stripper can be h0rny)
            elif choice in ['9', 'exit']:
                print("Exiting...")
                break
            elif choice == 'urltamper':
                tamperer.start()
            elif choice in ['start', 'restart', 'start menu']:
                self.start()  # Go back to the start menu
            elif choice == 'start menu':
                self.start()
            elif choice in ['change', 'border', 'change border']:
                border.change()
            else:
                print("Invalid choice. Please select a valid option.")

    def required_commands(self):
        print("Required = commands:")
#class initializations 
border = Border()
startup = Startup(border.style)
menus = Menus(border.style)  
qol = QoL(border.style)
converter = Converter(border.style)
tamperer = Tamperer(border.style)
stripper = Stripper(border.style)


#end of menus
if __name__ == "__main__":
#checks to see if a border has been preset via config file NaruZKurai.encoder.config.txt
#if none makes one, if broken makes new one, then sets the scripts border. retains changed borders
    startup.start()
#planned idea to do modes ex binary mode: various things that could be used for binary.
    menus.converter() 
