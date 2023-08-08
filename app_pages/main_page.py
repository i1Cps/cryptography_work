import customtkinter as ctk
# Widgets
from app_widgets.nav_bar import NavBar
from app_widgets.dark_mode_button import DarkModeButton
from app_widgets.text_box import TextBox
from app_widgets.contact_bar import ContactBar

class MainPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=('#b9bfc1','#4a2146'))
        self.parent = parent
        # Navigation bar has a relative width of 0.2
        self.nav_bar = NavBar(self, controller = parent, hidden= True)
        # Contact bar has relative width of 0.15
        self.contact_bar = ContactBar(self,controller=parent)
        self.dark_mode_button = DarkModeButton(self, controller=parent)
        self.dark_mode = True
        # Main frame has relative width 0.65
        # Create a frame to house the all the native SPN page widgets widgets
        self.main_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.main_frame.place(relx = 0.2, rely = 0, relheight = 1, relwidth  =0.65)
        
        welcome_message = 'Hello, Welcome to my Cryptography Portfolio. \nMy name is Theo Moore-Calters and I\'m a final ' \
            'year\n Computer Science student at the University of Bath'
        self.welcome_message = TextBox(self.main_frame, welcome_message, 20, height = 100, colour=('#cccccc', '#5c2958'))
    
    # Updates the toggle bar status from different pages
    def update_dark_mode(self,dark_mode):
        # If dark mode property is already set correctly do nothing
        if dark_mode == self.dark_mode:
            return
        # Update property and switch position 
        self.dark_mode = dark_mode
        # Command wont be triggered
        if dark_mode == True:
            self.dark_mode_button.switch.select()
        else:
            self.dark_mode_button.switch.deselect()
        
        