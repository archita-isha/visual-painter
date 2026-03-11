import cv2
import mediapipe as mp 

cap = cv2.VideoCapture(0)  # 0= default laptop camera 

while True:
    success , frame = cap.read()
    cv2.imshow("Camera",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()    

