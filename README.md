# Face-recognition-attendance-system

In many of the educational institutions, managing attendance of students/candidates is tedious as there would be a large number of students in the class and keeping track of all is onerous. Traditional system of marking attendance manually is very time consuming. For Handling this situation , Face recognition attendance system can be very helpful as it can automate the process of marking attendance of student. Face recognition is among the most productive image processing applications and has a pivotal role in the technical field. The development of this system is aimed to accomplish digitization of the traditional system of taking attendance by calling names and maintaining pen-paper records.

## ALGORITHM AND WORKING
Algorithm/ Technique used for this project is **HOG (Histogram of Gradients)**.
Face recognition using the Histogram of Oriented Gradients (HOG) algorithm is a robust technique that captures the local gradient patterns in images for accurate face detection and recognition. The HOG algorithm operates by extracting and analyzing the distribution of gradient orientations within a given image. 

**Working of HOG ALROGITHM :**

The HOG (Histogram of Gradients) technique counts occurrences of gradient orientation in the localized portion of an image. This method is quite similar to Edge Orientation Histograms and Scale Invariant aFeature Transformation (SIFT). The HOG descriptor focuses on the structure or the shape of an object. It is better than any edge descriptor as it uses magnitude as well as angle of the gradient to compute the features. For the regions of the image it generates histograms using the magnitude and orientations of the gradient.

There are 3 major steps involved in HOG algorithm :
  1. **Cellular Division :** - The basic idea of HOG is dividing the image into small connected cells
  2. **Calculating Gradients (direction x and y) :** - Gradients are the small change in the x and y directions. In this step we Compute histogram for each cell. It calculates gradients like small boxes containing information about the intensity of that portion . In short Information about the features of the face.
  3. **Formation of Feature Vector :** -  Bring all histograms together to form feature vector i.e., it forms one histogram from all small histograms which is unique for each face.  Optionally, the final feature vector can be further normalized across different blocks or the entire image to improve the robustness and discriminative power of the feature representation.
 
 For more detailed explanation reffer to this blogpost : https://medium.com/mlcrunch/face-detection-using-dlib-hog-198414837945  
 
## PROJECT WORKING AND INTERFACE

This project is built in a form of a software/ Graphical User Interface using 2 main libraries : **Tkinter & CustomTkinter**
The base GUI looks like the following : 

![Base GUI](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/1.png)

User has the flexibility to use dark theme , white theme or leave it as system default . Also user can scale the GUI to his/her preference .These features are made possible using CustomTkinter on top of Tkinter.

### REGISTRATION FRAME

This frame appears as the default frame whenever the application is opened . It can be found on the Right most side of the application. This Frame focuses on attaining / collecting students data whenever a new student is registered into a department. This process is usually performed when a new student is admitted.

<img src="https://github.com/Himanshu584/face-recognition-attendance-system/assets/70319246/06f37a89-13e3-4e45-b226-65f3f92c38e3" width='500px' height='250px' style="margin-left: 20px">

Upon filling the required details when a student clicks on the capture student button a camera window will open up that will allow for capturing the face of the student being registered. 

<img alt="capturing student" src="https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/3.png" width='550px' height='300px'>

The data of the registered student is stored inside a csv file. Also the image of student captured gets stored inside the images folder in the format of “ROLL_NUMBER.JPG”

![registered student](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/5.png)

### DELETION FRAME

On clicking the delete student button, the deletion frame gets activated where user can delete a student by entering student's roll number as input.
If the roll number entered is not present in the database, it will show no student found otherwise it will delete the student's information from student database and also image of the student.

<img alt="delete unknown student" src="https://github.com/Himanshu584/face-recognition-attendance-system/assets/70319246/2cc030ac-0f1b-43b2-8e37-c6ba00831182" width="450px" height="350px" >

<img alt="delete unknown student" src="https://github.com/Himanshu584/face-recognition-attendance-system/assets/70319246/1463835d-24fa-4078-8c17-80e09943c871" width="450px" height="350px" >



### MARKING ATTENDANCE STEP 

This is the final and the most important part of the entire project and Graphical user interface. On clicking the “Mark Attendance” Button , another Graphic window pops out.

**1st Frame : INITIALIZATION FRAME**

![initialization frame](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/initialization-frame.png)

During this frame, the algorithm is searching for a face in the video frame. when it finds the face , it moves on to next step.

**2nd Frame : MARKING FRAME**

![marking frame](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/marking-frame.png)

During this frame, the algorithm compares the encodings of the face found in video frame with the encodings of all faces present in the database and calculated the face distances. 

**3rd Frame : MARKED FRAME**

![marked frame](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/marked-frame.png)

After the face distances have been calculated, the face which had the minimum distance (highest probable face) is marked as present 

**4th Frame : ALREADY MARKED FRAME**

![already marked frame](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/already-marked-frame.png)

If someone whose attendance has already been marked comes in front of camera again , the system instead of marking the attendance again will simply tell the user that his/her attendance has already been marked.

After the marking of attendance has been completed, User can simply get the marked attendance in form of csv file in the attendance folder of project.

![attendance sheet](https://github.com/Himanshu584/face-recognition-attendance-system/blob/main/Project_imgs/6.png)


## To Run this project in your device ,follow the following steps 
1. clone the repository - ` git clone https://github.com/Himanshu584/face-recognition-attendance-system/ `
2. install the required dependancies - ` pip install requirements.txt `
3. Run the project - first cd into the project folder and run command : `python gui.py`

(*Use of Virtual environment is suggested)

# THANKYOU !
