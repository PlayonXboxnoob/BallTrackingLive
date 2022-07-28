import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture(0)
#scaling factor
scaling_factor = 0.5
# Loop until you hit the Esc key
while True:
    # Capture the current frame
    ret, frame = cap.read()
# Resize the frame
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
# Display the image
    cv2.imshow('Webcam', frame)
# Detect if the Esc key has been pressed
    c = cv2.waitKey(1)
    if c == 27:
        break

detector = PoseDetector()
posList = []
while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ''
        for lm in lmList:
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[3]},'
        posList.append(lmString)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])