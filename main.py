import cv2
import dlib

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW) 
cap.set(3,1280)
cap.set(4,720)


while True: 
    success, img = cap.read() 
    cv2.imshow("Attendance System",img)
    cv2.waitKey(1)
    if cv2.getWindowProperty("Attendance System",cv2.WND_PROP_VISIBLE) <1:
        break
cap.release()
cv2.destroyAllWindows()

