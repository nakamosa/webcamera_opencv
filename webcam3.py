import cv2
import numpy as np

image = cv2.imread("km.jpg", 0)
height = image.shape[0]
width = image.shape[1]
white = cv2.imread("white.png", 0)
white = cv2.resize(white,(round(width),round(height)))
image = cv2.medianBlur(image, 5)
gray_image = cv2.cvtColor(white, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 20, param1=60, param2=30, minRadius=5, maxRadius=30)
circles = np.uint16(np.around(circles))

j = 1

def abc(image):
    ret,thresh = cv2.threshold(image,127,255,0)
    imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    
    x,y,w,h = cv2.boundingRect(cnt)
    image = cv2.imread("white.png", 0)
    image = cv2.resize(image,(round(width),round(height)))
    img = cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
    
    ret,thresh = cv2.threshold(image,127,255,0)
    imgEdge,contours,hierarchy = cv2.findContours(thresh, 1, 2)
    cnt = contours[0]
    
    perimeter = cv2.arcLength(cnt,True)
    len = round(perimeter/4)
    
    return len




for i in circles[0, :]:
    cv2.circle(white, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #cv2.putText(white, str(j), (i[0]-13, i[1]+10), cv2.FONT_ITALIC, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
    cv2.namedWindow("img", cv2.WINDOW_NORMAL)
    cv2.imshow("img", white)
    len = abc(white)
    print(len ,"px")
    white = cv2.imread("white.png", 0)
    white = cv2.resize(white,(round(width),round(height)))
    cv2.waitKey(0)
    j = j + 1

cv2.namedWindow("img", cv2.WINDOW_NORMAL)
cv2.imshow("img", white)
cv2.waitKey(0)
cv2.destroyWindow()
