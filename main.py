import cv2
import os
import pickle 
import numpy as np
import face_recognition

# get video from the webcam
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(3,550) # set width of videocapture
cap.set(4,250) # set height of videocapture


background = cv2.imread("resources/BASE.png")  # background design
modes_folder = os.listdir("resources/modes") # mode path
modelist = []
# get all modes into model
for file in modes_folder:
    modelist.append(cv2.imread("resources/modes/" + file))

# load the encodings file 
with open("encodings.p","rb") as f:
    encodingwithids = pickle.load(f)

encodingslist, encodingids = encodingwithids

while True: 
    success, img = cap.read() 
    
    simg = cv2.resize(img,(0,0),None,0.25,0.25) # rescale the image to be computationally comfortable
    simg = cv2.cvtColor(simg,cv2.COLOR_BGR2RGB)

    # get current face from simg
    currface = face_recognition.face_locations(simg)
    currfaceencoding = face_recognition.face_encodings(simg,currface) # get encoding for only current face in simg

    # display graphics
    background[110:110+288,100:100+352] = img # set the video frame from webcam onto bg
    background[0:0+500,550:550+444] = modelist[1]

    # compare faces with face encodings and get most probable face 
    for faceencoding,currfacelocation in zip(currfaceencoding,currface):
        matches = face_recognition.compare_faces(encodingslist,faceencoding)
        facedis = face_recognition.face_distance(encodingslist,faceencoding)

        matchindex = np.argmin(facedis)
        print(matchindex)
        


    cv2.imshow("Attendance System",background)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Attendance System",cv2.WND_PROP_VISIBLE) <1:
        break
    
cap.release()
cv2.destroyAllWindows()

    

