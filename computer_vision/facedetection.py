import cv2

# adding out cascade
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

# Read an image
img = cv2.imread("Resources/uso.jpg")

# convert image to grayscale
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# find the faces in the image

face = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# create a bounding boz across the faces detected
# loop through all the faces in the image provided
# define the starting point
# define the corner points for every single face that will be detected after excecution
# define a colour
# define thickness of the line

for (x,y,w,h) in face:
    cv2.rectangle(img, (x,y),(x+w, y+h), (255,0,0),2)
    cv2.putText(img, "face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)

#Show/Display it
cv2.imshow("Faces", img)

#delay
cv2.waitKey(0)