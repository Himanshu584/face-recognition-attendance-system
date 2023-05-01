import cv2
import face_recognition
import os
import pickle

# load student images 
imgdir = "images"
studentimglist = []
studentimgids = []

# get all images of students into studentimglist
for img_pth in os.listdir(imgdir):
    studentimglist.append(cv2.imread(os.path.join(imgdir,img_pth)))
    studentimgids.append(img_pth.split('.')[0]) # get relative ids of students into studentimgids

print(len(studentimglist))
# encoding generator function
def encodeimages(studentimages):
    faceencodinglist = []
    for img in range(0,len(studentimages)):
        student = cv2.cvtColor(studentimages[img],cv2.COLOR_BGR2RGB)  # convert bgr to rbg
        encoding = face_recognition.face_encodings(student)[0] # encoding of single face
        faceencodinglist.append(encoding)
    return faceencodinglist


# # calling encoding generator function
face_encodings = encodeimages(studentimglist)
encodingswithids = [face_encodings,studentimgids]


# dump all the encodings with ids into pickle/pascal file
with open("encodings.p",'wb') as f:
    pickle.dump(encodingswithids,f)

    
