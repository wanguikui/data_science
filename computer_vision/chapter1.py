import cv2

#print("Package Installed")

# reading image
#img = cv2.imread("Resources/pic1.jpg")
# display the image
#cv2.imshow("Image",img)
# setting a delay
#cv2.waitKey(0)

# importing videos
#cap = cv2.VideoCapture("Resources/sheng.mp4")

# read video

#while True:

    #success, img = cap.read()
    #cv2.imshow("Video", img)

    #if cv2.waitKey(25) & 0xFF ==ord('q'):
        #break

# Use Webcam

webcam = cv2.VideoCapture(0)

# Set the size
webcam.set(3,640)
webcam.set(4,480)
# adjust brightness
webcam.set(10, 100)
while True:
    success, img = webcam.read()

    cv2.imshow("Kui", img)
    if cv2.waitKey(25) & 0xFF ==ord('q'):
        break

