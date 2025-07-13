import cv2
import numpy as np
circles = np.zeros((4,2),int)
counter = 0

def mousePoints(event,x,y,flags,params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter+1
        print(circles)

img = cv2.imread("D:\python\openCV\cards.jpg")
while True:
    if counter == 4:
        width,height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("output",imgOutput)
    
    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)
        cv2.imshow("original image",img)
        cv2.setMouseCallback("original image",mousePoints)
    key = cv2.waitKey(1)
    if key == 27:  # Press 'Esc' to close the window
        break
    