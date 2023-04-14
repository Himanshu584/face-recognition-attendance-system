import tkinter as tk
import customtkinter
import os
from PIL import Image as pilimg
from PIL import ImageTk as imtk
from csv import writer
import cv2
import capture_student
import pandas as pd
import time



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

        self.department_entry = customtkinter.CTkEntry(self.register_frame, placeholder_text="Department")
        self.department_entry.grid(row=3, column=1, columnspan=3, padx=(20, 20), pady=(10, 20), sticky="ew")

        self.register_capture = customtkinter.CTkButton(master=self.register_frame,text="Capture Student", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"), command=self.register_student)
        self.register_capture.grid(row=4, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")


        # - DELETE STUDENT FRAME - #
        self.delete_student_frame = customtkinter.CTkFrame(self,width=950,corner_radius=0)

        self.delete_logo_label = customtkinter.CTkLabel(self.delete_student_frame,text="Delete  Student", font=customtkinter.CTkFont(size=30, weight="bold"))
        self.delete_logo_label.grid(row=0,column=1,padx=(29,29), pady=(20, 20), sticky="nsew")

        self.student_roll = customtkinter.CTkEntry(self.delete_student_frame,placeholder_text="Roll Number")
        self.student_roll.grid(row=1, column=1, columnspan=2, padx=(20, 20), pady=(10, 20), sticky="nsew")  

        self.delete_student_bttn = customtkinter.CTkButton(master=self.delete_student_frame,text="Delete Student", fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"),command=lambda :self.delete_student(int(self.student_roll.get())))
        self.delete_student_bttn.grid(row=4, column=1, padx=(20, 20), pady=(10, 10), sticky="nsew")
        
        self.deleted_student_display = customtkinter.CTkLabel(master=self.delete_student_frame,text="")
        self.deleted_student_display.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
        ### -------------- ###




    # Frame changing function
    def select_frame_by_name(self, name):
        """show selected frame in column 3 of main grid"""
        if name == "Register":
            self.register_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        else:
            self.register_frame.grid_forget()
        if name == "delete_student":
            self.delete_student_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        else:
            self.delete_student_frame.grid_forget()

    # Work Functions

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # register section functions
    def register_button_event(self):
        """ activates the register frame for registering new student """
        self.select_frame_by_name("Register")

    def register_student(self):
        """takes students information and stores it in a file, then turns on front camera to capture students photo"""
        
        # storing student information into a list
        student_data = [self.name_entry.get(),self.rollnum_entry.get(),self.department_entry.get()]
        # writing the student information into student_database
        with open("student_db/students.csv",'a') as f_obj:
            writer_object = writer(f_obj)
            writer_object.writerow(student_data)
            f_obj.close()

        # clear the input fields 
        self.name_entry.delete(0,customtkinter.END)
        self.rollnum_entry.delete(0,customtkinter.END)
        self.department_entry.delete(0,customtkinter.END)

        # capturing student image
        capture_student.App(tk.Toplevel(), "Capture Student Image",roll_num=student_data[1])


    # delete section functions
    def delete_button_event(self):
        """ Activates the delete student frame to delete a student """
        self.select_frame_by_name("delete_student")
        self.deleted_student_display.grid_forget()

    def delete_student(self,roll_number):
        """ takes roll_number and deletes student's photo and information from database """
        self.student_roll.delete(0,customtkinter.END)
        # read student database into pandas dataframe
        self.student_data = pd.read_csv("student_db/students.csv")

        if roll_number in self.student_data['roll_num'].values :
            # student info
            self.dname = self.student_data[self.student_data["roll_num"]==roll_number]['name'][0]
            self.droll = self.student_data[self.student_data["roll_num"]==roll_number]['roll_num'][0]
            self.ddept = self.student_data[self.student_data["roll_num"]==roll_number]['department'][0]

            ## deleting the student from database and images

            # filtering data to exclude rows with roll Number given
            self.student_data = self.student_data[self.student_data["roll_num"] !=roll_number]
            # delete required students photo from images folder
            os.remove("images/{}.jpg".format(roll_number))

            # write filtered data back to csv file
            self.student_data.to_csv("student_db/students.csv",index=False,columns=['name','roll_num','department'])

            self.deleted_student_display = customtkinter.CTkLabel(master=self.delete_student_frame,text="Deleted Student :\n\nName:\t {} \n Roll Number:\t {}\n Department:\t {}".format(self.dname,self.droll,self.ddept))
            self.deleted_student_display.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")
            # self.deleted_student_display.configure(text="Deleted Student :\n\nName:\t {} \n Roll Number:\t {}\n Department:\t {}".format(self.dname,self.droll,self.ddept))
        else:
            self.deleted_student_display = customtkinter.CTkLabel(master=self.delete_student_frame,text="No student with roll number {}".format(roll_number))
            self.deleted_student_display.grid(row=5, column=1, padx=(10, 10), pady=(10, 10), sticky="ew")

        



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
