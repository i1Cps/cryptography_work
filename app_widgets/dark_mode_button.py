import customtkinter as ctk
from PIL import Image

# Navigation bar for navigating the app
class DarkModeButton(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent, fg_color='transparent', width = 250)
        self.parent = parent
        self.dark_mode = True
        switch_var = ctk.StringVar(value="on")
        self.switch = ctk.CTkSwitch(self,
                               text = "",
                               fg_color='#4a2146',
                               progress_color='#b9bfc1',

                               command = lambda: self.toggle_dark_mode(controller),
                               variable = switch_var,
                               onvalue = "on",
                               offvalue="off",
                               switch_height = 20,
                               switch_width = 50,
                               corner_radius= 10
                            )
        self.switch.pack(expand= True, fill = 'both', padx = 5)
        
        # Places button in parent frame
        self.place(relx=0.93,rely=0, relheight = 0.05)
    
    def toggle_dark_mode(self, controller):
        # Update properties for widget and parent page
        self.dark_mode = not self.dark_mode
        self.parent.dark_mode = not self.parent.dark_mode
        # Toggle dark mode
        controller.toggle_dark_mode()
   