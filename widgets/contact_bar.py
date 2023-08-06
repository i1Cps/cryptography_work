import customtkinter as ctk
from PIL import Image

# Contact bar for contact information
class ContactBar(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent, fg_color='transparent')
        # Import icons
        self.open_menu_img = ctk.CTkImage(
            light_image= Image.open('assets/menu.png'),
            dark_image = Image.open('assets/purple_menu.png'),
            size=(30,30))
        self.close_menu_img = ctk.CTkImage(
            light_image = Image.open('assets/close.png'),
            dark_image =  Image.open('assets/purple_cross.png'),
            size=(30,30))
        # Places navigation bar in parent frame
        self.place(relx=0.85,rely=0,relheight= 1, relwidth = 0.15)
        
   