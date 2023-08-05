import customtkinter as ctk
# Widgets
from widgets.nav_bar import NavBar
from widgets.dark_mode_button import DarkModeButton
from widgets.text_box import TextBox
from widgets.contact_bar import ContactBar

class MainPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=('#b9bfc1','#4a2146'))
        # Navigation bar has a relative width of 0.2
        self.nav_bar = NavBar(self, controller = parent, hidden= True)
        self.dark_mode_button = DarkModeButton(self, controller=parent)
        # Contact bar has relative width of 0.15
        self.contact_bar = ContactBar(self,controller=parent)
        # Main frame has relative width 0.65
        # Create a frame to house the all the native SPN page widgets widgets
        self.main_frame = ctk.CTkFrame(self, fg_color='blue')
        self.main_frame.place(relx = 0.2, rely = 0, relheight = 1, relwidth  =0.65)
        
        welcome_message = 'Hello, Welcome to my Cryptography Portfolio. \nMy name is Theo Moore-Calters and I\'m a final ' \
            'year\n Computer Science student at the University of Bath'
        self.welcome_message = TextBox(self.main_frame, welcome_message, 20, height = 100)
        
        #self.create_widgets()
        #self.create_layout()
    
    """ def create_widgets(self):
        self.menu_button1 = ctk.CTkButton(self, text = 'SPN Implementation')
        self.menu_button2 = ctk.CTkButton(self, text = 'Cryptoanalysis Implementation')
        self.menu_button3 = ctk.CTkButton(self, text = '')
        
    # Setup grid layout for menu
    def create_layout(self):
        self.columnconfigure((0), weight=1)
        self.rowconfigure((0,1,2), weight=1)

        self.menu_button1.grid(row=0, sticky = 'nswe', pady = 2, padx = 20)
        self.menu_button2.grid(row=1, sticky = 'nswe', pady = 0)
        self.menu_button3.grid(row=2, sticky = 'nswe', pady = 20)
        
        #self.entry.place(relx=0.5,rely=0.95, relwidth=0.9) """