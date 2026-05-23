# pip install opencv-python
# pip install mediapipe
import cv2
import mediapipe as mp

# track face hands and body pose together
mp_holistic = mp.solutions.holistic
mp_draw = mp.solutions.drawing_utils
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)


# load pre-trained haar Cascade face detector
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# start webcam, try 1 or 2 if you have multiple cameras
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Could not open webcam.")
    exit()

while True:
    # read frame
    ret, frame = cap.read()

    # cam might drop frames occasionally, don't crash when it does
    if not ret or frame is None:
        print("Error: Failed to read frame.")
        break

    # face detector only works on grayscale 
    # color info just slows it down
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100,100)) # 30x30

    if len(faces) > 0:
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (203, 192, 255), 2) # changed the colour colour to pink :0

    cv2.imshow("Face Detection", frame)

    # close with Q or the X button
    # close with Q or the X button
    if cv2.waitKey(1) & 0xFF == ord("q") or cv2.getWindowProperty("Face Detection", cv2.WND_PROP_VISIBLE) < 1:
        break
    

# cleanup to release cam so other apps can use it again
cap.release()
cv2.destroyAllWindows()
