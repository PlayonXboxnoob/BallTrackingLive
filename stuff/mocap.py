import cv2
from cvzone.PoseModule import PoseDetector
import socket

host, port = "127.0.0.1", 25001
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

#cap = cv2.VideoCapture('Vid.mp4')
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

success, img = cap.read()
#path = 'C://Users//adity//OneDrive//Desktop//mprof//Assets//AnimationFile.txt'
#f = open(path, 'w')

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

        #f.write(lmString)
        #f.write('\n')
        #f.flush()
        posList.append(lmString)


        sock.sendall(lmString.encode("UTF-8"))
        receivedData = sock.recv(1024).decode("UTF-8")
        print(receivedData)

    print(len(posList))

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    if key == ord('s'):
        #with open("AnimationFile.txt", 'w') as f:
        #    f.writelines(["%s\n" % item for item in posList])
        #f.close()
        break