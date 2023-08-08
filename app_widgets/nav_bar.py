import customtkinter as ctk
from PIL import Image

# Navigation bar for navigating the app
class NavBar(ctk.CTkFrame):
    def __init__(self, parent, controller, hidden):
        super().__init__(master=parent, fg_color='transparent', width = 150)
        self.controller = controller
        self.parent = parent
        # Import icons
        self.open_menu_img = ctk.CTkImage(
            light_image= Image.open('app_assets/menu.png'),
            dark_image = Image.open('app_assets/purple_menu.png'),
            size=(30,30))
        self.close_menu_img = ctk.CTkImage(
            light_image = Image.open('app_assets/close.png'),
            dark_image =  Image.open('app_assets/purple_cross.png'),
            size=(30,30))
        # Animation variables
        self.hidden = hidden
        self.start_position = -1.0
        self.end_position = 0
        self.width = abs(self.start_position - self.end_position)
        self.wrong_icon = False
        self.animating = False
        self.current_position = self.start_position if self.hidden else self.end_position
        self.y_pos = 0.15        
        # Create widgets
        self.create_navigation_option_widgets()
        self.create_toggle_widget()
        self.create_layout()
        self.selected_button(self.main_page_button)
        # Places navigation bar in parent frame
        self.place(relx=0,rely=0,relheight= 1, relwidth = 0.2)
        
    def create_toggle_widget(self):
        self.toggle_button_frame = ctk.CTkFrame(self, fg_color=('#cccccc','#5c2958'))
        self.toggle_nav_bar_button = ctk.CTkButton(self.toggle_button_frame,
                                                   text='',
                                                   image= self.open_menu_img if self.hidden else self.close_menu_img,
                                                   compound='left',
                                                   height=50,
                                                   width=50,
                                                   corner_radius=10,
                                                   fg_color='transparent',
                                                   hover_color=('#b9bfc1','#4a2146'),
                                                   command=lambda: self.animate())
        
    # Function controls the layout of navigation bar
    def create_navigation_option_widgets(self):
        # Create Frame to hold menu options
        self.options_frame    = ctk.CTkFrame(self, fg_color='transparent',width = 15, height = 40)
        self.page_buttons = []
        self.main_page_button = ctk.CTkButton(self.options_frame, 
                                              fg_color='transparent', 
                                              height=80, text= 'Main', 
                                              text_color=('#2e152c','#cccccc'), 
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5, 
                                              command = lambda : self.change_page('MainPage',self.main_page_button))
        self.page_buttons.append(self.main_page_button)
        self.spn_page_button  = ctk.CTkButton(self.options_frame,
                                              fg_color='transparent',
                                              height=80,
                                              text= 'Substitution\nPermutation\nNetwork',
                                              text_color=('#2e152c','#cccccc'),
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5,
                                              command = lambda : self.change_page('SPNPage', self.spn_page_button))
        self.page_buttons.append(self.spn_page_button)
        self.cryptoanalysis_page_button = ctk.CTkButton(self.options_frame,
                                              fg_color='transparent',
                                              state= 'disabled',
                                              height=80,
                                              text= 'Cryptoanalysis',
                                              text_color=('#2e152c','#cccccc'),
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5)
        self.page_buttons.append(self.cryptoanalysis_page_button)
        self.data_encryption_standard_page_button = ctk.CTkButton(self.options_frame,
                                              fg_color='transparent',
                                              state= 'disabled',
                                              height=80,
                                              text= 'Data\nEncryption\nStandard',
                                              text_color=('#2e152c','#cccccc'),
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5)
        self.page_buttons.append(self.data_encryption_standard_page_button)
        self.advanced_encryption_algorithm_page_button = ctk.CTkButton(self.options_frame,
                                              fg_color='transparent',
                                              state='disabled',
                                              height=80,
                                              text= 'Advanced\nEcntryption\nStandard',
                                              text_color=('#2e152c','#cccccc'),
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5)
        self.page_buttons.append(self.advanced_encryption_algorithm_page_button)
        self.hash_functions_page_button = ctk.CTkButton(self.options_frame,
                                              fg_color='transparent',
                                              state='disabled',
                                              height=80,
                                              text= 'Hash Functions',
                                              text_color=('#2e152c','#cccccc'),
                                              text_color_disabled=('#6d5b6b','#b9bfc1'),
                                              hover_color=('#3693ec','#2667a5'),
                                              corner_radius=5)
        self.page_buttons.append(self.hash_functions_page_button)
        
    
    # Function places all widgets in the navigation bar
    def create_layout(self):
        # Toggle
        self.toggle_button_frame.place(x= 5, rely=0, relheight = 0.1, relwidth = 0.94)
        self.toggle_nav_bar_button.pack(side='left', padx = 5)
        # Menu
        self.options_frame.place(relx = self.current_position, rely=self.y_pos, relwidth = self.width, relheight = 0.9)
        self.main_page_button.pack(ipadx = 5, padx = 5)
        self.spn_page_button.pack(ipadx = 5, padx = 5)
        self.cryptoanalysis_page_button.pack(ipadx = 5, padx = 5)
        self.data_encryption_standard_page_button.pack(ipadx = 5, padx = 5 )
        self.advanced_encryption_algorithm_page_button.pack(ipadx = 5, padx = 5 )
        self.hash_functions_page_button.pack(ipadx = 5, padx = 5 )
    
    def change_page(self,selected_page, selected_page_button):
        # Switch to selected page
        self.controller.show_page(selected_page,self.parent.dark_mode)
        # Set all other navigation bar buttons to 'non selected colour'
        for page_button in self.page_buttons:
            page_button.configure(fg_color='transparent')
        self.selected_button(selected_page_button)
        
    def selected_button(self,selected_page_button):
        # set given navigation bar button to 'selected colour'
        selected_page_button.configure(fg_color=('#cccccc', '#5c2958'))
        
    # Animation for navigation bar
    def animate(self):
        # stops function call if its currently animating
        if not self.animating:
            self.animating = True
            self.wrong_icon = True
            if self.hidden:
                self.animate_on_screen()
            else:
                self.animate_off_screen()
                
    # Toggles navigation bar ON
    def animate_on_screen(self):
        if self.current_position < self.end_position:
            self.current_position += 0.025
            self.options_frame.place(relx = self.current_position, rely=self.y_pos, relwidth = self.width, relheight = 1)
            if self.wrong_icon:
                self.toggle_nav_bar_button.configure(image = self.close_menu_img)
                self.wrong_icon = False
            self.after(10, self.animate_on_screen)
        else:
            self.hidden = False
            self.animating = False
    
    # Toggles Navigation bar OFF
    def animate_off_screen(self):
        if self.current_position > self.start_position:
            self.current_position -= 0.025
            self.options_frame.place(relx = self.current_position, rely = self.y_pos, relwidth = self.width, relheight = 1)
            if self.wrong_icon:
                self.toggle_nav_bar_button.configure(image = self.open_menu_img)
                self.wrong_icon = False
            self.after(10, self.animate_off_screen)
        else:
            self.hidden = True
            self.animating = False
        
        

        
