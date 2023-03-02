import tkinter as tk
import os

# create the main window
width = 600
height = 300
root = tk.Tk()
root.geometry("{}x{}".format(width,height))
root.title("Face Recognition System")

# defining the button functions
def add():
    print("Registering new faces...")

def train():
    print("Training the system...")
    os.system("python encoder.py")

def detect():
    print("Detecting faces...")
    os.system(" python main.py")

def delete():
    print("Deleting faces...")

def report():
    print("Generating csv file...")

# creating the buttons
train_button = tk.Button(root, text="Train", command=train)
train_button.pack(side=tk.LEFT)

detect_button = tk.Button(root, text="Detect", command=detect)
detect_button.pack(side= tk.RIGHT)

add_button = tk.Button(root, text="Add", command=add)
add_button.pack(side= tk.LEFT)

delete_button = tk.Button(root, text="Delete", command=delete)
delete_button.pack(side=tk.RIGHT)

gen_report_button = tk.Button(root,text="Generate Attendance",command=report)
gen_report_button.pack(side=tk.BOTTOM)

# start the main event loop
root.mainloop()
