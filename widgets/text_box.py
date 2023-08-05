import customtkinter as ctk
from PIL import Image

# Navigation bar for navigating the app
class TextBox(ctk.CTkFrame):
    def __init__(self, parent, message, text_size, width=50, height=350, corner_radius=10, 
                 colour = ('#cccccc', '#5c2958')):
        super().__init__(master=parent, fg_color=colour, width=width, height=height, corner_radius=corner_radius)
        
        font = ctk.CTkFont(family='Luckiest Guy', size=text_size)
        self.text_box = message = ctk.CTkLabel(self,
                                            text=message,
                                            font=font,
                                            #justify = 'center',
        
                                            corner_radius=10)
        
        self.text_box.pack(expand=True, side='top', pady= 10)
        self.pack( ipady = 0, pady = 0, padx = 10, fill = 'both')
        
    def update_text(self, new_text):
        self.text_box.configure(text=new_text)
        
        
   