import tkinter
import tkinter.messagebox
import customtkinter
import os
from PIL import Image as pilimg



customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Face Recognition Attendance System - Himanshu Sharma")
        self.geometry(f"{1100}x{580}")
        self.resizable(0,0)

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        # self.grid_columnconfigure((2), weight=1)
        self.grid_rowconfigure((1), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Select Options", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # attendance system buttons
        self.register_button = customtkinter.CTkButton(self.sidebar_frame,text="Register Student", command=self.register_button_event)
        self.register_button.grid(row=1, column=0, padx=20, pady=10)

        self.delete_button = customtkinter.CTkButton(self.sidebar_frame,text="Delete Student", command=self.delete_button_event)
        self.delete_button.grid(row=2, column=0, padx=20, pady=10)

        self.train_button = customtkinter.CTkButton(self.sidebar_frame,text="Train Model", command=self.train_button_event)
        self.train_button.grid(row=3, column=0, padx=20, pady=10)

        self.detect_button = customtkinter.CTkButton(self.sidebar_frame,text="Mark Attendance", command=self.detect_button_event)
        self.detect_button.grid(row=4, column=0, padx=20, pady=10)

        self.report_button = customtkinter.CTkButton(self.sidebar_frame,text="generate Attendance",command=self.report_button_event)
        self.report_button.grid(row=5, column=0, padx=20, pady=10)
        
        # appearance buttons
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        # # COLUMN-2 CONFIGURATION (INFO SECTION)
        self.info_label = customtkinter.CTkLabel(self,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=customtkinter.CTkFont(size=25, weight="bold"))
        self.info_label.grid(row=0,column=1,padx=(20,20), pady=(20, 10), sticky="ew")

        self.attendance_gui_img = customtkinter.CTkImage(pilimg.open('resources/attendance_gui.jpg'),size=(600,600))
        self.central_image = customtkinter.CTkLabel(self,text=" ",image=self.attendance_gui_img)
        self.central_image.grid(row=1,column=1,padx=(20,20),pady=(20,30),sticky="nsew")

        self.progressbar_1 = customtkinter.CTkProgressBar(self)
        self.progressbar_1.grid(row=3, column=1, padx=(20, 10), pady=(10, 10), sticky="ew")
        self.progressbar_1.start()
        self.progressbar_1.configure(mode="indeterminnate")

        ### ------ column-3 configurations -------- ###

        # - REGISTER STUDENT FRAME - #
        self.register_frame = customtkinter.CTkFrame(self, width=940, corner_radius=0)
        self.register_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        
        self.logo_label = customtkinter.CTkLabel(self.register_frame, text="Register Student", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=1, padx=(20,20), pady=(20, 20), sticky="ew")

        # create main entry and button
        self.name_entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Name")
        self.name_entry.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

        self.rollnum_entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Roll Number")
        self.rollnum_entry.grid(row=2, column=1, columnspan=2, padx=(20, 20), pady=(10, 20), sticky="ew")

        self.entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Course")
        self.entry.grid(row=3, column=1, columnspan=3, padx=(20, 20), pady=(10, 20), sticky="ew")

        self.register_capture = customtkinter.CTkButton(master=self.register_frame,text="Capture Student", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.register_capture.grid(row=4, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")


        # - DELETE STUDENT FRAME - #
        self.delete_student_frame = customtkinter.CTkFrame(self,width=950,corner_radius=0)

        self.delete_logo_label = customtkinter.CTkLabel(self.delete_student_frame,text="Delete  Student", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.delete_logo_label.grid(row=0,column=1,padx=(29,29), pady=(20, 20), sticky="nsew")

        self.student_roll = customtkinter.CTkEntry(self.delete_student_frame,placeholder_text="Roll Number")
        self.student_roll.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(10, 20), sticky="nsew")

        self.delete_student_bttn = customtkinter.CTkButton(master=self.delete_student_frame,text="delete Student", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        self.delete_student_bttn.grid(row=4, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        ### -------------- ###




    # Frame changing function
    def select_frame_by_name(self, name):
        # set button color for selected button
    #     self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
    #     self.frame_2_button.configure(fg_color=("gray75", "gray25") if name == "frame_2" else "transparent")
        # self.frame_3_button.configure(fg_color=("gray75", "gray25") if name == "frame_3" else "transparent")

    #     # show selected frame
        if name == "Register":
            self.register_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        else:
            self.register_frame.grid_forget()
        if name == "delete_student":
            self.delete_student_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        else:
            self.delete_student_frame.grid_forget()
    #     if name == "frame_3":
    #         self.third_frame.grid(row=0, column=1, sticky="nsew")
    #     else:
    #         self.third_frame.grid_forget()

    # Work Functions

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def register_button_event(self):
        """ Registers new student """
        self.select_frame_by_name("Register")
    
    def delete_button_event(self):
        """deletes the student data we want to delete"""
        self.select_frame_by_name("delete_student")


    def train_button_event(self):
        """runs the encoder.py file .i.e generates the face encodings for students in database"""
        print("Training the system...")
        # os.system("python encoder.py")
    
    def detect_button_event(self):
        print("Marking Attendance")
        os.system("python main.py")
    
    def report_button_event(self):
        """Generates attendace sheet for the day"""
        print("Generating csv file...")


if __name__ == "__main__":
    app = App()
    app.mainloop()





















# import tkinter
# import customtkinter as ctk
# import os

# ctk.set_appearance_mode("dark")
# # ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
# ctk.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

# app = ctk.CTk()  # create CTk window like you do with the Tk window
# app.title("face-recognition-attendance-system")
# app.geometry("400x500")
# app.resizable(0,0)

# # functions 
# def appear_light():
#     """sets the gui theme to light mode"""
#     ctk.set_appearance_mode("light")
#     title_label.configure(font=("Roboto",20,"bold"),text_color="#37694e")
#     print("light theme activated")

# def appear_dark():
#     """sets the gui theme to dark mode"""
#     ctk.set_appearance_mode("dark")
#     title_label.configure(font=("Roboto",20,"bold"),text_color="#42f595")
#     print("dark theme activated")

# def register_student():
#     """registers new student in database/folder. Collects student information and captures there faces with format = 'rollnumber.jpg/png'"""
#     print("Registering new faces...")

# def train_model():
#     """runs the encoder.py file .i.e generates the face encodings for students in database"""
#     print("Training the system...")
#     os.system("python encoder.py")

# def detect_face():
#     """runs main.py file, it detects and marks students attendance"""
#     print("Detecting faces...")
#     os.system("python main.py")

# def delete_face():
#     """deletes the student we want to delete"""
#     print("Deleting faces...")

# def report():
#     """Generates attendace sheet for the day"""
#     print("Generating csv file...")

# # ,fg_color="#f542e6"
# # title
# title_label = ctk.CTkLabel(master=app,text="Face Recognition Attendance System",text_color="#42f595")
# title_label.place(relx=0.5,rely=0.1,anchor=tkinter.CENTER)
# title_label.configure(font=("Roboto",20,"bold"))

# # buttons
# register_button = ctk.CTkButton(master=app, text="Register",command=register_student)
# register_button.place(relx=0.5,rely=0.2,anchor=tkinter.N)
# register_button.configure(font=("Roboto",15,"bold"))



# train_button = ctk.CTkButton(master=app, text="Train",command=train_model)
# train_button.place(relx=0.5,rely=0.3,anchor=tkinter.N)
# train_button.configure(font=("Roboto",15,"bold"))

# detect_button = ctk.CTkButton(master=app, text="Mark",command=detect_face)
# detect_button.place(relx=0.5,rely=0.4,anchor=tkinter.N)
# detect_button.configure(font=("Roboto",15,"bold"))

# delete_button = ctk.CTkButton(master=app, text="Delete",command=delete_face)
# delete_button.place(relx=0.5,rely=0.5,anchor=tkinter.N)
# delete_button.configure(font=("Roboto",15,"bold"))

# report_button = ctk.CTkButton(master=app, text="Report",command=report)
# report_button.place(relx=0.5,rely=0.6,anchor=tkinter.N)
# report_button.configure(font=("Roboto",15,"bold"))


# # Theme Buttons
# light_button = ctk.CTkButton(master=app, text="light Theme", command=appear_light)
# light_button.place(relx=0.45, rely=0.9, anchor=tkinter.E)
# light_button.configure(font=("Roboto",15,"bold"))

# dark_button = ctk.CTkButton(master=app, text="Dark Theme", command=appear_dark)
# dark_button.place(relx=0.55,rely=0.9,anchor=tkinter.W)
# dark_button.configure(font=("Roboto",15,"bold"))

# app.mainloop()