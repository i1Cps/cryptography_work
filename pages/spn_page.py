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
        self.main_frame = ctk.CTkFrame(self, fg_color='blue',width=630)
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
        self.cipher_text = cipher_text = 0b0111000011010100
        
        self.create_widgets()
        self.create_layout()
    
    def create_widgets(self):
        # Key
        key_display_value = 'Key: ' + self.spn.pad_bits(bin(self.key),32)
        self.key_entry_button = ctk.CTkButton(self.spn_frame,
                                              fg_color=('#cccccc', '#5c2958'),
                                              text='Change key value',
                                              border_color=('#5c2958','#cccccc'),
                                              command=lambda: self.open_input_dialog_event())
        self.key_label = TextBox(self.spn_frame,key_display_value, 15)
        
        # Encryption and Decryption
        # create tabview
        self.encryptdecrypt = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        
        #self.spn.pad_bits(bin(self.key)
        
    # Setup grid layout for menu
    def create_layout(self):
        #self.key_entry.pack(side='top')
        self.key_label.pack(side='top',fill='y')
        self.key_entry_button.pack(side='top')
        
    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Enter your key:", title="Chane the key")
        self.key = bin(int(dialog.get_input(),2))
        key_display_value = 'Key: ' + self.key[2:]
        self.key_label.update_text(key_display_value)
        
        print("CTkInputDialog:", self.key)
        
    def run(self):
        # Create SPN 
        substitution_permutation_network = SPN(debug=True)
        # Change key below 
        key = 0b11100111011001111001000000111101
        # Change plain text below
        plain_text = 0b0100111010100001
        # Change the cipher text below
        cipher_text = 0b0111000011010100

        # Encrypt
        try:
            #substitution_permutation_network.encrypt(plain_text, key)
            substitution_permutation_network.encrypt(cipher_text, key)
        except ValueError as err:
            print(err) 
                
