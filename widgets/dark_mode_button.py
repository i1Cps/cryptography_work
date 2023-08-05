import customtkinter as ctk
from PIL import Image

# Navigation bar for navigating the app
class DarkModeButton(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(master=parent, fg_color='transparent', width = 250)
        
        switch_var = ctk.StringVar(value="on")
        switch = ctk.CTkSwitch(self,
                               text = "",
                               fg_color='#4a2146',
                               progress_color='#b9bfc1',

                               command = lambda: controller.toggle_dark_mode(),
                               variable = switch_var,
                               onvalue = "on",
                               offvalue="off",
                               switch_height = 20,
                               switch_width = 50,
                               corner_radius= 10
                            )
        switch.pack(expand= True, fill = 'both', padx = 5)
        
        # Places button in parent frame
        self.place(relx=0.93,rely=0, relheight = 0.05)
        
   