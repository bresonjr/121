import cv2  
import numpy as np  
  
video = cv2.VideoCapture(0) 
image = cv2.imread("EB.jpg") 

bg = 1

for i in range(60):
    ret, bg = video.read()

bg = np.flip(bg, axis=1)

while True: 
  
    ret, frame = video.read() 
    print(frame)
    frame = cv2.resize(frame, (640, 480)) 
    image = cv2.resize(image, (640, 480)) 

    l_black = np.array([65, 60, 60])
    u_black = np.array([80, 255,255])
    mask_1 = cv2.inRange(frame, lower_white, upper_green)

    lower_white = np.array([104, 153, 70])
    upper_green = np.array([250, 250, 250])
    mask_2 = cv2.inRange(frame, lower_white, upper_green)

    mask = mask_1 + mask_2

    res = cv2.bitwise_and(frame, frame, mask = mask) 


    f = frame - res 
    f = np.where(f == 0, image, f) 
  
    cv2.imshow("video", frame) 
    cv2.imshow("mask", f) 
  
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break 
  
video.release() 
cv2.destroyAllWindows()