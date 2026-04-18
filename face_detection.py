import cv2

# load pre-trained Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# start webcam
cap = cv2.VideoCapture(0)

while True:
    # read frame
    ret, frame = cap.read()

    # convert to grayscale (required for detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # draw rectangles around faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame,
                      (x, y),
                      (x + w, y + h),
                      (255, 0, 0),
                      2)

    # show output
    cv2.imshow("Face Detection", frame)

    # press Q to quit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# cleanup
cap.release()
cv2.destroyAllWindows()