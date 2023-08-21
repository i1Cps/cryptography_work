import customtkinter as ctk
# Widgets
from app_widgets.nav_bar import NavBar
from app_widgets.dark_mode_button import DarkModeButton
from app_widgets.text_box import TextBox
from app_widgets.contact_bar import ContactBar
# Cryptography
from cryptography.Substitution_Permutation_Network import SPN
# Binary helper function
from cryptography.helpers.binary_helper import BinaryHelper

class SPNPage(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent, fg_color=('#b9bfc1','#4a2146'))
        self.parent = parent
        self.nav_bar = NavBar(self, controller = parent, hidden=False)
        self.contact_bar = ContactBar(self, controller=parent)
        self.dark_mode_button = DarkModeButton(self, controller=parent)
        self.dark_mode = True
        
        # Create a frame to house the all the native SPN page widgets widgets
        self.main_frame = ctk.CTkFrame(self, fg_color='transparent',width=630)
        self.main_frame.place(relx = 0.2, rely = 0, relheight = 1, relwidth = 0.65)
        
        # Add welcome message
        welcome_message = 'Welcome to my Substitution Permutation Network (SPN)\nimplementation'
        self.welcome_text_box = TextBox(self.main_frame, welcome_message, 20,colour=('#cccccc', '#5c2958'))
        self.welcome_text_box.pack_configure( )
        
        # Add seperate frame to hold SPN components
        self.spn_frame = ctk.CTkFrame(self.main_frame, fg_color=('#cccccc', '#5c2958'),width=630)
        self.spn_frame.pack(fill = 'both', expand=True, pady = 10, padx = 10,side = 'top')
        
        # Add SPN description
        cipher_information = 'An SPN is a block cipher construction employing substitution and\n ' + \
        'permutation operations in repeated rounds. Though effective,\nSPNs are susceptible to ' + \
        'a technique\ncalled cryptoanalysis, leading to advancements in more secure encryption\n' + \
        'techniques. Such as the Data Encryption\nStandard and the Advanced Encryption Standard'
        self.cipher_infomation_box= TextBox(self.main_frame,cipher_information, 14, colour=('#cccccc', '#5c2958'))
        
        # SPN properties
        self.spn = SPN()
        self.key = 0b11100111011001111001000000111101
        
        self.plain_text = 0b0100111010100001
        self.cipher_text = 0b0111000011010100
        
        # Helper function
        self.binary_helper_function = BinaryHelper()
        
        self.create_widgets()
        self.create_layout()
        
    def create_widgets(self):
        # Key
        self.key_entry_button = ctk.CTkButton(self.spn_frame,
                                              fg_color=('#cccccc', '#4a2146'),
                                              text='Change key value',
                                              font=ctk.CTkFont(family='Luckiest Guy', size=15), 
                                              text_color=('#000000','#ffffff'),
                                              border_color=('#4a2146','#cccccc'),
                                              command=lambda: self.input_custom_key())
        key_display_value = 'Key: ' + bin(self.key)[2:] + ' (32 bits)'
        self.key_label = TextBox(self.spn_frame,key_display_value, 15, colour=('#cccccc', '#5c2958'))
        
        
        # Encryption and Decryption tabs
        self.encryptdecrypt = ctk.CTkTabview(self.spn_frame, width=250, fg_color=('#b9bfc1','#4a2146'))
        self.encryptdecrypt.add("Encrypt")
        self.encryptdecrypt.add("Decrypt")
        self.encryptdecrypt.tab("Encrypt").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.encryptdecrypt.tab("Decrypt").grid_columnconfigure(0, weight=1)
        
        # Plain Text and cipher text
        self.plain_text_entry_button = ctk.CTkButton(self.encryptdecrypt.tab('Encrypt'),
                                              fg_color=('#cccccc', '#4a2146'),
                                              text='Change the plain text value',
                                              font=ctk.CTkFont(family='Luckiest Guy', size=15), 
                                              text_color=('#000000','#ffffff'),
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.input_custom_plain_text())
        self.cipher_text_entry_button = ctk.CTkButton(self.encryptdecrypt.tab('Decrypt'),
                                              fg_color=('#cccccc', '#4a2146'),
                                              text='Change the cipher text value',
                                              font=ctk.CTkFont(family='Luckiest Guy', size=15), 
                                              text_color=('#000000','#ffffff'),
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.input_custom_cipher_text())
        #plain_text_display_value = 'Plain Text: ' + self.spn.pad_bits(bin(self.plain_text),16)
        plain_text_display_value = 'Plain Text: ' + bin(self.plain_text)[2:] + ' (16 bits)'
        cipher_text_dispaly_value = 'Cipher Text: ' + bin(self.cipher_text)[2:] + ' (16 bits)'
        self.plain_text_label = TextBox(self.encryptdecrypt.tab('Encrypt'), plain_text_display_value, 15, side='top', colour=('#cccccc', '#5c2958'))
        self.cipher_text_label = TextBox(self.encryptdecrypt.tab('Decrypt'), cipher_text_dispaly_value, 15, colour=('#cccccc', '#5c2958'))
        
        
        # Encypt and decrypt buttons
        self.encrypt_button = ctk.CTkButton(self.encryptdecrypt.tab('Encrypt'),
                                            fg_color=('#cccccc', '#5c2958'),
                                              text='Encrypt',
                                              font=ctk.CTkFont(family='Luckiest Guy', size=15), 
                                              text_color=('#000000','#ffffff'),
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.run_encryption())
        # Encypt and decrypt buttons
        self.decrypt_button = ctk.CTkButton(self.encryptdecrypt.tab('Decrypt'),
                                            fg_color=('#cccccc', '#5c2958'),
                                              text='Decrypt',
                                              font=ctk.CTkFont(family='Luckiest Guy', size=15), 
                                              text_color=('#000000','#ffffff'),
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.run_decryption())
        
        self.encrypted_plain_text = TextBox(self.encryptdecrypt.tab('Encrypt'), '', 15, side='bottom', colour=('#cccccc', '#5c2958'))
        self.encrypted_plain_text.pack_configure(pady=5)
        self.decrypted_cipher_text = TextBox(self.encryptdecrypt.tab('Decrypt'), '', 15, side = 'bottom', colour=('#cccccc', '#5c2958'))
        self.decrypted_cipher_text.pack_configure(pady=5)
        #self.decrypted_cipher_text.configure(pady=5)
        #self.spn.pad_bits(bin(self.key)
        
    # Setup grid layout for menu
    def create_layout(self):
        #self.key_entry.pack(side='top')
        self.key_label.pack(side='top',fill='y')
        
        self.key_entry_button.pack(side='top')
        self.plain_text_entry_button.pack(pady = 10)
        self.cipher_text_entry_button.pack(pady=10)
        self.encryptdecrypt.pack(expand=True,side = 'top', fill='both', padx = 10, pady = 15)
        self.encrypt_button.pack(side='top', expand=True, fill='both', padx = 180, pady=5)
        self.decrypt_button.pack(side='top', expand=True, fill='both', padx = 180, pady=5)
        
        
    # Function gets input for custom key
    def input_custom_key(self):
        dialog = ctk.CTkInputDialog(text="Enter your key:", title="Change the key")
        input = dialog.get_input()
        # Error handling for non binary numbers
        if not self.binary_helper_function.is_binary_number(input):
            print('not a bianry input')
            return
        # Error handling for keys longer than 32 bits
        if len(input) > 32:
            print('key input bigger than 32 bits')
            return
        # Pad custom key to 32 bits
        add_padding = self.spn.pad_bits(bin(int(input,2)),32)
        # Convert to int (SPN class will handle int -> bin conversionn)
        self.key = int(add_padding,2)
        # Display the padded string representation to show the full 32 bits
        key_display_value = 'Key: ' + add_padding[2:] + ' (32 bits)'
        self.key_label.update_text(key_display_value)
        
    def input_custom_plain_text(self):
        dialog = ctk.CTkInputDialog(text="Enter your plain text:", title="Change the plain text")
        input = dialog.get_input()
        # Error handling for non binary numbers
        if not self.binary_helper_function.is_binary_number(input):
            print('not a binary input')
            return
        # Error handling for plain text longer than 16 bits
        if len(input) > 16:
            print('Plain text is bigger than 16 bits')
            return
        # Pad custom plain text to 16 bits
        add_padding = self.spn.pad_bits(bin(int(input,2)),16)
        # Convert to int (SPN class will handle int -> bin conversionn)
        self.plain_text = int(add_padding,2)
        # Display the padded string representation to show the full 16 bits
        plain_text_display_value = 'Plain Text: ' + add_padding[2:] + ' (16 bits)'
        self.plain_text_label.update_text(plain_text_display_value)
        
    def input_custom_cipher_text(self):
        dialog = ctk.CTkInputDialog(text="Enter your cipher text:", title="Change the cipher text")
        input = dialog.get_input()
        # Error handling for non binary numbers
        if not self.binary_helper_function.is_binary_number(input):
            print('not a binary input')
            return
        if len(input) > 16:
            print('cipher text is bigger thtan 16 bits')
            return
        # Pad custom cipher textd
        add_padding = self.spn.pad_bits(bin(int(input,2)),16)
        # Convert to int (SPN class will handle int -> bin conversionn)
        self.cipher_text = int(add_padding,2)
        cipher_text_display_value = 'Cipher Text: ' + add_padding[2:] + ' (16 bits)'
        self.cipher_text_label.update_text(cipher_text_display_value)
        
    def run_encryption(self):
        # Encrypt
        try:
            self.spn.encrypt(self.plain_text, self.key)
            self.encrypted_plain_text.update_text('Encrypted Text: ' + self.spn.cipher_text[2:])
            self.encrypted_plain_text.pack(side='bottom',pady = 5)
        except ValueError as err:
            print(err) 
    
    def run_decryption(self):
        # Decrypt
        try:
            self.spn.decrypt(self.cipher_text, self.key)
            self.decrypted_cipher_text.update_text('Decrypted Text: ' + self.spn.plain_text[2:])
            self.decrypted_cipher_text.pack(side='bottom', pady=5)
        except ValueError as err:
            print(err)
            
    # Updates the toggle bar status from different pages
    def update_dark_mode(self,dark_mode):
        if dark_mode == self.dark_mode:
            return
        # Update property and switch position 
        self.dark_mode = dark_mode
        # Command wont be triggered
        if dark_mode == True:
            self.dark_mode_button.switch.select()
        else:
            self.dark_mode_button.switch.deselect()
        
        
                
