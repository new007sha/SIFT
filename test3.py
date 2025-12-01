import cv2
cap=cv2.VideoCapture(0)
sift=cv2.SIFT_create()
while True :
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    Keypoints,descriptors=sift.detectAndCompute(gray,None)
    frame=cv2.drawKeypoints(frame,Keypoints,frame,flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
    cv2.imshow("mapping",frame)
    if cv2.waitKey(1)&0xFF==ord(' '):
        break
cap.release()
cv2.destroyAllWindows()   