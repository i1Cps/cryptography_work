import customtkinter as ctk
from PIL import Image

# Contact bar for contact information
class ContactBar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent, fg_color='transparent')
        
        # Places navigation bar in parent frame
        self.place(relx=0.85,rely=0,relheight= 1, relwidth = 0.15)
        
   