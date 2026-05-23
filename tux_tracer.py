# pip install opencv-python
# pip install mediapipe
import cv2
import mediapipe as mp
import numpy as np

# add tux with all 3 years of concepts drawn as his trace
# tux = cv2.imread("tux.png", cv2.IMREAD_UNCHANGED)

def tint_pink(img):
    # change colour of my tux transparent image 
    result = img.copy()
    result[:, :, 0] = 203  # B
    result[:, :, 1] = 192  # G
    result[:, :, 2] = 255  # R
    return result

tux = cv2.imread("tux.png", cv2.IMREAD_UNCHANGED)
tux = tint_pink(tux)  # made tux pink :)

def overlay_image(frame, img, x, y, size=20):
    img = cv2.resize(img, (size, size))
    h, w = img.shape[:2]

    if x < 0 or y < 0 or x + w > frame.shape[1] or y + h > frame.shape[0]:
        return frame
    if img.shape[2] == 4:
        alpha = img[:, :, 3] / 255.0
        for c in range(3):
            frame[y:y+h, x:x+w, c] = (alpha * img[:, :, c] + (1-alpha) * frame[y:y+h, x:x+w, c])
    else:
        frame[y:y+h, x:x+w] = img
    return frame
# track face hands and body pose together
mp_holistic = mp.solutions.holistic
mp_draw = mp.solutions.drawing_utils
holistic = mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# changed the traces to be in pink :)
pink = (203, 192, 255)
pink_dot = mp_draw.DrawingSpec(color=pink, thickness=1, circle_radius=1)
pink_line = mp_draw.DrawingSpec(color=pink, thickness=2, circle_radius=2)

cap = cv2.VideoCapture(0)

# load pre-trained haar Cascade face detector
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

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
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = holistic.process(rgb)

    if results.face_landmarks:
        h, w, _ = frame.shape
        for i, landmark in enumerate(results.face_landmarks.landmark):
            if i % 468== 0:
                x = int(landmark.x * w)
                y = int(landmark.y * h)
                frame = overlay_image(frame, tux, x - 150, y - 150, size=300)

    # drawing mesh around face 
    # dot cloud on face
    # if results.face_landmarks:
    #    mp_draw.draw_landmarks(frame, results.face_landmarks, mp_holistic.FACEMESH_CONTOURS, pink_dot, pink_dot)

    # drawing hand landmarks 
     if results.left_hand_landmarks:
        mp_draw.draw_landmarks(frame, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS, pink_line, pink_dot)

     if results.right_hand_landmarks:
        mp_draw.draw_landmarks(frame, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, pink_line, pink_dot)

    # then body pose like shoulders, elbows, wrists etc. 
     if results.pose_landmarks:
        mp_draw.draw_landmarks(frame, results.pose_landmarks, mp_holistic.POSE_CONNECTIONS, pink_line, pink_dot)

    

    # face detector only works on grayscale 
    # color info just slows it down
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100,100)) # 30x30

   # if len(faces) > 0:
   #     for (x, y, w, h) in faces:
   #         cv2.rectangle(frame, (x, y), (x + w, y + h), (203, 192, 255), 2) # changed the colour colour to pink :0

    cv2.imshow("Tux Tracer", frame)

    # close with Q or the X button
    if cv2.waitKey(1) & 0xFF == ord("q") or cv2.getWindowProperty("Tux Tracer", cv2.WND_PROP_VISIBLE) < 1:
        break
    

# cleanup to release cam so other apps can use it again
holistic.close()
cap.release()
cv2.destroyAllWindows()
