# Modules
import tkinter as tk
import customtkinter as ctk

# Pages in the app (frames)
from app_pages.main_page import *
from app_pages.spn_page import  *

class App(ctk.CTk):
    def __init__(self, title, size):
        # 'APP' Class inherits from CTk class (Its a 'Main app window')
        super().__init__()
        # Main setup
        ctk.set_appearance_mode('dark')
        self.dark_mode = True
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
        self.maxsize(size[0] + 200, size[1])
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)
        
        # Pages logic
        self.all_pages = {}
        
        # Iterating through a tuple consisting
        # of the different pages
        
        for P in (MainPage,SPNPage):
            page = P(self)
            self.all_pages[P.__name__] = page
            # initializing each page in app
            page.grid(row=0, column=0, sticky='nwse')
        
        # Starts app with main page
        self.show_page('MainPage')
        
        # Run
        self.mainloop()
        
    # Function that changes app to specified page
    def show_page(self,page_name, dark_mode = True):
        page = self.all_pages[page_name]
        # Updates the dark mode switch status for new opened pages
        page.update_dark_mode(dark_mode)
        page.tkraise()
    
    # Function that toggles dark mode on or off 
    def toggle_dark_mode(self):
        if self.dark_mode:
            # Switch to light mode
            ctk.set_appearance_mode('light')
            self.dark_mode = False
        else:
            # Switch to dark mode
            ctk.set_appearance_mode('dark')
            self.dark_mode = True
              
App('Cryptography Work', (1000,600))

