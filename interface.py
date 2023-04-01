# import customtkinter
# import os
# import cv2
# from PIL import Image,ImageTk


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("image_example.py")
#         self.geometry("700x450")

#         # set grid layout 1x2
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(1, weight=1)

#         # load images with light and dark mode image
#         image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "images")
#         self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "17332029002.jpg")), size=(26, 26))
#         self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "17332029004.jpg")))
#         self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "17332029005.jpg")))
#         self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "17332029007.jpg")),
#                                                  dark_image=Image.open(os.path.join(image_path, "17332029007.jpg")), size=(20, 20))
#         self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "17332029023.jpg")),
#                                                  dark_image=Image.open(os.path.join(image_path, "17332029023.jpg")), size=(20, 20))
#         self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "17332029028.jpg")),
#                                                      dark_image=Image.open(os.path.join(image_path, "17332029028.jpg")), size=(20, 20))

#         # create navigation frame
#         self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
#         self.navigation_frame.grid(row=0, column=0, sticky="nsew")
#         self.navigation_frame.grid_rowconfigure(4, weight=1)

#         self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  Image Example", image=self.logo_image,
#                                                              compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
#         self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

#         self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Home",
#                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
#                                                    image=self.home_image, anchor="w", command=self.home_button_event)
#         self.home_button.grid(row=1, column=0, sticky="ew")

#         self.frame_2_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 2",
#                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
#                                                       image=self.chat_image, anchor="w", command=self.frame_2_button_event)
#         self.frame_2_button.grid(row=2, column=0, sticky="ew")

#         self.frame_3_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Frame 3",
#                                                       fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
#                                                       image=self.add_user_image, anchor="w", command=self.frame_3_button_event)
#         self.frame_3_button.grid(row=3, column=0, sticky="ew")

#         self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
#                                                                 command=self.change_appearance_mode_event)
#         self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=20, sticky="s")

#         # create home frame
#         self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
#         self.home_frame.grid_columnconfigure(0, weight=1)

#         self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
#         self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

#         self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="", image=self.image_icon_image)
#         self.home_frame_button_1.grid(row=1, column=0, padx=20, pady=10)
#         self.home_frame_button_2 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="right")
#         self.home_frame_button_2.grid(row=2, column=0, padx=20, pady=10)
#         self.home_frame_button_3 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="top")
#         self.home_frame_button_3.grid(row=3, column=0, padx=20, pady=10)
#         self.home_frame_button_4 = customtkinter.CTkButton(self.home_frame, text="CTkButton", image=self.image_icon_image, compound="bottom", anchor="w")
#         self.home_frame_button_4.grid(row=4, column=0, padx=20, pady=10)

#         # create second frame
#         self.second_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
#         self.imglabel = customtkinter.CTkLabel(self.second_frame,bg_color="blue")
#         self.imglabel.grid(row=1,column=1,padx=(20,0),pady=(10,0))



#         self.second_fbutton = customtkinter.CTkButton(self.second_frame,text="secondframe",command= self.dekhlebhai)
#         self.second_fbutton.grid(row=2,column=1,padx=(20,0),pady=(10,0))

#         # create third frame
#         self.third_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
#         self.name = customtkinter.CTkEntry(self.third_frame,placeholder_text="Name: ")
#         self.name.grid(row=2,column=1)

#         self.third_fbutton = customtkinter.CTkButton(self.third_frame,text="secondframe",command=self.huhum)
#         self.third_fbutton.grid(row=3,column=1,padx=(20,0),pady=(10,0))
#         # self.third_frame.configure(state="disabled")

#         # select default frame
#         self.select_frame_by_name("home")



#     def select_frame_by_name(self, name):
#         # set button color for selected button
#         self.home_button.configure(fg_color=("gray75", "blue") if name == "home" else "transparent")
#         self.frame_2_button.configure(fg_color=("gray75", "blue") if name == "frame_2" else "transparent")
#         self.frame_3_button.configure(fg_color=("gray75", "blue") if name == "frame_3" else "transparent")

#         # show selected frame
#         if name == "home":
#             self.home_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.home_frame.grid_forget()
#         if name == "frame_2":
#             self.second_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.second_frame.grid_forget()
#         if name == "frame_3":
#             self.third_frame.grid(row=0, column=1, sticky="nsew")
#         else:
#             self.third_frame.grid_forget()

#     def home_button_event(self):
#         self.select_frame_by_name("home")

#     def frame_2_button_event(self):
#         self.select_frame_by_name("frame_2")

#     def frame_3_button_event(self):
#         self.select_frame_by_name("frame_3")

#     def change_appearance_mode_event(self, new_appearance_mode):
#         customtkinter.set_appearance_mode(new_appearance_mode)

#     def huhum(self):
#         if self.name.get() != "":
#             print(self.name.get())

#     def dekhlebhai(self):
#         self.cap = cv2.VideoCapture(0)
#         while True:
#             self.img = self.cap.read()[1]
#             self.img1 = cv2.cvtColor(self.img,cv2.COLOR_BGR2RGB)
#             self.img = ImageTk.PhotoImage(Image.fromarray(self.img1))
#             self.imglabel['image'] = self.img
#             self.second_frame.update()
#         self.cap.release()


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()








# # from tkinter import *
# # import os

# # # create the main window
# # width = 750
# # height = 500
# # root = Tk()
# # root.geometry("{}x{}".format(width,height))
# # root.resizable(0,0)
# # root.config(bg="black")
# # root.title("Face Recognition System")
# # root.columnconfigure(2,weight=1)
# # root.rowconfigure(7,weight=2)

# # # defining the button functions
# # def register():
# #     print("Registering new faces...")

# # def train():
# #     print("Training the system...")
# #     os.system("python encoder.py")

# # def detect():
# #     print("Detecting faces...")
# #     os.system("python main.py")

# # def delete():
# #     print("Deleting faces...")

# # def report():
# #     print("Generating csv file...")

# # # title label
# # title_label = Label(root,text="Face Recognition Attendance System",fg="pink",bg="black")
# # title_label.grid(row=0,column=1,columnspan=2)
# # title_label.config(font=("Roboto",25,"bold"))
# # # creating the buttons

# # # register a new student
# # register_button = Button(root, text="Add",fg="white",bg="black",width=10,height=3,command=register)
# # register_button.grid(row=3,column=2,pady=(15,0))
# # register_button.config(font=("Roboto", 10, "bold"))

# # # train model on registered student
# # train_button = Button(root, text="Train",fg="white",bg="black",width=10,height=3, command=train)
# # train_button.grid(row=4,column=2,pady=(15,0))
# # train_button.config(font=("Roboto", 10, "bold"))

# # # Mark attendance 
# # detect_button = Button(root, text="Mark",fg="white",bg="black",width=10,height=3, command=detect)
# # detect_button.grid(row=5,column=2,pady=(15,0))
# # detect_button.config(font=("Roboto", 10, "bold"))

# # # Generate Attendance Sheet
# # gen_report_button = Button(root,text="Report",fg="white",bg="black",width=10,height=3,command=report)
# # gen_report_button.grid(row=6,column=2,pady=(15,0))
# # gen_report_button.config(font=("Roboto",10,"bold"))

# # proccess_tracker = Label(root, text="hgh")
# # proccess_tracker.grid(row=7)
# # # start the main event loop
# # root.mainloop()



# capture after few seconds
import cv2
import time
   
  
# SET THE COUNTDOWN TIMER
# for simplicity we set it to 3
# We can also take this as input
TIMER = int(10)
   
# Open the camera
cap = cv2.VideoCapture(0)
   
  
while True:
      
    # Read and display each frame
    ret, img = cap.read()
    cv2.imshow('a', img)
  
    # check for the key pressed
    k = cv2.waitKey(125)
  
    # set the key for the countdown
    # to begin. Here we set q
    # if key pressed is q
    if k == ord('q'):
        prev = time.time()
  
        while TIMER >= 0:
            _, img = cap.read()
  
            # Display countdown on each frame
            # specify the font and draw the
            # countdown using puttext
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(img, str(TIMER), 
                        (150, 200), font,
                        7, (0, 255, 255),
                        4, cv2.LINE_AA)
            cv2.imshow('a', img)
            cv2.waitKey(125)
  
            # current time
            cur = time.time()
  
            # Update and keep track of Countdown
            # if time elapsed is one second 
            # then decrease the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
  
        else:
            _, img = cap.read()
  
            # Display the clicked frame for 2 
            # sec.You can increase time in 
            # waitKey also
            cv2.imshow('a', img)
  
            # time for which image displayed
            cv2.waitKey(1000)
  
            # Save the frame
            cv2.imwrite('camera.jpg', img)
  
            # HERE we can reset the Countdown timer
            # if we want more Capture without closing
            # the camera
  
    # Press Esc to exit
    elif k == 27:
        break
  
# close the camera
cap.release()
   
# close all the opened windows
cv2.destroyAllWindows()


