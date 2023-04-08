import cv2
import os
import tkinter as tk
from PIL import Image, ImageTk

# Function to capture photo from front camera and save it
def capture_photo(name, roll, department, name_entry, roll_entry, department_entry, camera_window):
    # Open the front camera
    cap = cv2.VideoCapture(0)

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Create a directory to store the photos if it doesn't exist
    if not os.path.exists('photos'):
        os.mkdir('photos')

    # Save the photo with the student's name in the photos directory
    photo_path = f"photos/{name}_{roll}_{department}.jpg"
    cv2.imwrite(photo_path, frame)

    # Release the camera
    cap.release()

    # Clear the input fields in the GUI window
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    department_entry.delete(0, tk.END)

    # Close the camera window
    camera_window.destroy()

# Function to start the camera and display the live video feed in a new window
def start_camera(name_entry, roll_entry, department_entry):
    # Create a new window
    camera_window = tk.Toplevel()
    camera_window.title("Capture Photo")

    # Create a label to display the live video feed
    label = tk.Label(camera_window)
    label.pack()

    # Create a button to capture the photo
    button = tk.Button(camera_window, text="Capture", command=lambda: capture_photo(name_entry.get(), roll_entry.get(), department_entry.get(), name_entry, roll_entry, department_entry, camera_window))
    button.pack()

    # Start the camera and update the label with each captured frame
    cap = cv2.VideoCapture(0)
    while True:
        # Capture a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to a PIL Image
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)

        # Convert the PIL Image to a Tkinter PhotoImage
        photo = ImageTk.PhotoImage(img)

        # Update the label in the Tkinter interface with the PhotoImage
        label.config(image=photo)
        label.image = photo

        # Update the Tkinter interface and wait for 1 millisecond
        camera_window.update()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera
    cap.release()
    cv2.destroyAllWindows()

# Create a Tkinter window for getting student information
root = tk.Tk()
root.title("Student Information")

# Create a label for the student's name
name_label = tk.Label(root, text="Name:")
name_label.pack()

# Create an entry widget for the student's name
name_entry = tk.Entry(root)
name_entry.pack()

# Create a label for the student's roll number
roll_label = tk.Label(root, text="Roll Number:")
roll_label.pack()

# Create an entry widget for the student's roll number
roll_entry = tk.Entry(root)
roll_entry.pack()

# Create a label for the student's department
department_label = tk.Label(root, text="Department:")
department_label.pack()

# Create an entry widget for the student's department
department_entry = tk.Entry(root)
department_entry.pack()

# Create a button to start camera
capture_button = tk.Button(root, text="Capture Photo", command=lambda: start_camera(name_entry, roll_entry, department_entry))
capture_button.pack()

root.mainloop()