import cv2
import tkinter as tk
import customtkinter
from PIL import Image, ImageTk


class VideoCapture:
    def __init__(self, video_source=0):
        self.video_source = video_source
        self.vid = cv2.VideoCapture(self.video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (False, None)

    def release(self):
        if self.vid.isOpened():
            self.vid.release()


class App:
    def __init__(self, window, window_title,roll_num, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.roll_num = roll_num

        # Open video source (by default this will try to open the computer webcam)
        self.vid = VideoCapture(self.video_source)

        # Create a canvas that can fit the above video source size
        self.canvas = tk.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()

        # Add a capture button
        self.capture_button = customtkinter.CTkButton(window, text="Capture", command=self.capture)
        self.capture_button.pack()

        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        # Bind the window close event to the release method of the VideoCapture object
        self.window.protocol("WM_DELETE_WINDOW", self.release)

        self.window.mainloop()

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.window.after(self.delay, self.update)

    def capture(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()

        if ret:
            # Save the frame as an image with the given roll number as the file name
            file_name = f"images/{self.roll_num}.jpg"
            cv2.imwrite(file_name, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

            # Close the program after capturing and saving the image
            self.release()

    def release(self):
        # Release the VideoCapture object and close the window
        self.vid.release()
        self.window.destroy()

