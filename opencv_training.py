import cv2

img=cv2.imread('pics/stimuli.png',1)
img=cv2.resize(img,(400,400))

cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 

cap=cv2.VideoCapture(0)

while True:
    ret, frame=cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))

    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #mask=cv2.inRange(hsv, lower_blue, upper_blue)
    #result=cv2.bitwise_and(frame, frame,mask=mask)

    cv2.imshow('frame', hsv)
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()