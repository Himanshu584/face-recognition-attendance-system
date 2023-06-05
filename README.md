# face-recognition-attendance-system

In many of the educational institutions, managing attendance of students/candidates is tedious as there would be a large number of students in the class and keeping track of all is onerous. Traditional system of marking attendance manually is very time consuming. For Handling this situation , Face recognition attendance system can be very helpful as it can automate the process of marking attendance of student. Face recognition is among the most productive image processing applications and has a pivotal role in the technical field. The development of this system is aimed to accomplish digitization of the traditional system of taking attendance by calling names and maintaining pen-paper records.

## RUNNING PROJECT



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
 




