import customtkinter as ctk
# Widgets
from widgets.nav_bar import NavBar
from widgets.dark_mode_button import DarkModeButton
from widgets.text_box import TextBox
from widgets.contact_bar import ContactBar
# Cryptography
from cryptography.Substitution_Permutation_Network import SPN

class SPNPage(ctk.CTkFrame):
    def __init__(self,parent):
        super().__init__(master=parent, fg_color=('#b9bfc1','#4a2146'))        
        self.nav_bar = NavBar(self, controller = parent, hidden=False)
        self.contact_bar = ContactBar(self, controller=parent)
        self.dark_mode_button = DarkModeButton(self, controller=parent)
        
        # Create a frame to house the all the native SPN page widgets widgets
        self.main_frame = ctk.CTkFrame(self, fg_color='transparent',width=630)
        self.main_frame.place(relx = 0.2, rely = 0, relheight = 1, relwidth = 0.65)
        
        # Add welcome message
        welcome_message = 'Welcome to my Substitution Permutation Network (SPN)\nimplementation'
        self.welcome_text_box = TextBox(self.main_frame, welcome_message, 20)
        self.welcome_text_box.pack_configure( )
        
        # Add seperate frame to hold SPN components
        self.spn_frame = ctk.CTkFrame(self.main_frame, fg_color=('#cccccc', '#5c2958'),width=630)
        self.spn_frame.pack(fill = 'both', expand=True, pady = 10, padx = 10,side = 'top')
        
        # Add SPN description
        cipher_information = 'An SPN is a block cipher construction employing substitution and\n ' + \
        'permutation operations in repeated rounds. Though effective,\nSPNs are susceptible to ' + \
        'a technique\ncalled cryptoanalysis, leading to advancements in more secure encryption\n' + \
        'techniques. Such as the Data Encryption\nStandard and the Advanced Encryption Standard'
        self.cipher_infomation_box= TextBox(self.main_frame,cipher_information, 14)
        
        # SPN properties
        self.spn = SPN()
        self.key = 0b11100111011001111001000000111101
        
        self.plain_text = 0b0100111010100001
        self.cipher_text = 0b0111000011010100
        
        self.create_widgets()
        self.create_layout()
    
    def create_widgets(self):
        # Key
        self.key_entry_button = ctk.CTkButton(self.spn_frame,
                                              fg_color=('#cccccc', '#4a2146'),
                                              text='Change key value',
                                              border_color=('#4a2146','#cccccc'),
                                              command=lambda: self.input_custom_key())
        key_display_value = 'Key: ' + self.spn.pad_bits(bin(self.key),32)
        self.key_label = TextBox(self.spn_frame,key_display_value, 15)
        
        
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
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.input_custom_key())
        self.cipher_text_entry_button = ctk.CTkButton(self.encryptdecrypt.tab('Decrypt'),
                                              fg_color=('#cccccc', '#4a2146'),
                                              text='Change the cipher text value',
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.input_custom_key())
        plain_text_display_value = 'Plain Text: ' + self.spn.pad_bits(bin(self.plain_text),16)
        cipher_text_dispaly_value = 'Cipher Text: ' + self.spn.pad_bits(bin(self.cipher_text),16)
        self.plain_text_label = TextBox(self.encryptdecrypt.tab('Encrypt'), plain_text_display_value, 15, side='top')
        self.cipher_text_label = TextBox(self.encryptdecrypt.tab('Decrypt'), cipher_text_dispaly_value, 15)
        
        
        # Encypt and decrypt buttons
        self.encrypt_button = ctk.CTkButton(self.encryptdecrypt.tab('Encrypt'),
                                            fg_color=('#cccccc', '#4a2146'),
                                              text='Encrypt',
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.run_encryption())
        # Encypt and decrypt buttons
        self.decrypt_button = ctk.CTkButton(self.encryptdecrypt.tab('Decrypt'),
                                            fg_color=('#cccccc', '#4a2146'),
                                              text='Decrypt',
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.run_decryption())
        
        self.encrypted_plain_text = TextBox(self.encryptdecrypt.tab('Encrypt'), '', 15, side='bottom')
        self.decrypted_cipher_text = TextBox(self.encryptdecrypt.tab('Decrypt'), '', 15, side = 'bottom')
        
        #self.spn.pad_bits(bin(self.key)
        
    # Setup grid layout for menu
    def create_layout(self):
        #self.key_entry.pack(side='top')
        self.key_label.pack(side='top',fill='y')
        
        self.key_entry_button.pack(side='top')
        self.plain_text_entry_button.pack()
        self.cipher_text_entry_button.pack()
        self.encryptdecrypt.pack(expand=True,side = 'top', fill='both', padx = 10, pady = 15)
        self.encrypt_button.pack(side='top', expand=True, fill='both')
        self.decrypt_button.pack()
        
        
        
    def input_custom_key(self):
        dialog = ctk.CTkInputDialog(text="Enter your key:", title="Change the key")
        self.key = bin(int(dialog.get_input(),2))
        key_display_value = 'Key: ' + self.key[2:]
        self.key_label.update_text(key_display_value)
        
    def input_custom_plain_text(self):
        dialog = ctk.CTkInputDialog(text="Enter your key:", title="Change the key")
        self.key = bin(int(dialog.get_input(),2))
        key_display_value = 'Key: ' + self.key[2:]
        self.key_label.update_text(key_display_value)
        
    def input_custom_cipher_text(self):
        dialog = ctk.CTkInputDialog(text="Enter your key:", title="Change the key")
        self.key = bin(int(dialog.get_input(),2))
        key_display_value = 'Key: ' + self.key[2:]
        self.key_label.update_text(key_display_value)
        
        
    def run_encryption(self):
        # Encrypt
        try:
            self.spn.encrypt(self.plain_text, self.key)
            self.encrypted_plain_text.update_text(self.spn.cipher_text)
            self.encrypted_plain_text.pack(side='bottom')
        except ValueError as err:
            print(err) 
    
    def run_decryption(self):
        # Decrypt
        try:
            self.spn.decrypt(self.cipher_text, self.key)
            self.decrypted_cipher_text.update_text(self.spn.plain_text)
            self.decrypted_cipher_text.pack(side='bottom')
        except ValueError as err:
            print(err) 
        
        
                
