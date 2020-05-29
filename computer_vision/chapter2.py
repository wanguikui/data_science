import cv2
import numpy as np
# change the colour setting of an image

# convert an image to grayscale
# blur an image
# present the edges of an image - Edge detector

# Taking a matrix of size 5 as the Kernel
kernel = np.ones((5,5), np.uint8)

img = cv2.imread("Resources/pic1.jpg")
cv2.imshow("Image", img)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(img, (9,9),0)
imgcanny = cv2.Canny(img,100,100)
imgErosion = cv2.erode(img, kernel, iterations=1)
imgDilation = cv2.dilate(img, kernel, iterations=1)
imgDraw = cv2.rectangle(img,(30,30),(300,260),(0,255,0),5)
imgWrite = cv2.drawChessboardCorners

#cv2.imshow("Image Gray", imgGray)
#cv2.imshow("Image Blur" , imgBlur)
#cv2.imshow("Edges", imgcanny)
#cv2.imshow("Erosion", imgErosion)
#cv2.imshow("Dilation", imgDilation)
#cv2.imshow("Draw", imgDraw)


#Research Erode an image,
# Dilate an image, 
# Draw an image
blankImg =  np.zeros((512,512,3), np.uint8)
#print(blankimg.shape)

rectangle = cv2.rectangle(blankImg, (30, 30), (300, 200), (0, 255, 0), 5)
circle = cv2.circle(blankImg,(200,200),90,(0,20,200),10)
line = cv2.line(blankImg,(0,0),(300,300),(0,255,215),4)
text = cv2.putText(blankImg, " I am using OpenCV",(10,100),cv2.FONT_HERSHEY_COMPLEX, 2,(0,130,0),3)
cv2.imshow("Blank Image", blankImg)




# Cropping an image 
#imgCrop = img[0:200, 200:500]
#cv2.imshow("Cropped Image", imgCrop)
# Resizing an image 
#imgResize = cv2.resize(img, (300,200))
#cv2.imshow("Resized Image", imgResize)

cv2.waitKey(0)

# FaceRecognition app