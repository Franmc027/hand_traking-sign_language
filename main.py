import time
import cv2
import os
import HandTrackingModule as htm

WCAM, HCMA = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, WCAM)
cap.set(4, HCMA)

folderPath = 'Finguersimages'
myList = os.listdir(folderPath)
print(myList)
overlayList = []

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    overlayList.append(image)

pTime = 0

detector = htm.handDetector()

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # coordinates of the landmarks
    # print(lmList)
    image_index = 7

    if len(lmList) != 0:

        # A
        if lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and \
                lmList[20][2] > lmList[18][2] and lmList[4][2] < lmList[5][2]:
            image_index = 0
            print('The letter is: A')

        # E
        if lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and \
                lmList[20][2] > lmList[18][2] and lmList[7][2] < lmList[4][2]:
            image_index = 1
            print('The letter is: E')

        # I

        if lmList[8][2] > lmList[6][2] and lmList[12][2] > lmList[10][2] and lmList[16][2] > lmList[14][2] and \
                lmList[20][2] < lmList[18][2] and lmList[11][2] < lmList[4][2]:
            image_index = 2
            print('The letter is: I')

        # O
        if lmList[4][2] < lmList[8][2] < lmList[3][2] and lmList[4][2] < lmList[12][2] < lmList[3][2] and \
                lmList[4][2] < lmList[16][2] < lmList[3][2] and lmList[4][2] < lmList[20][2] < lmList[3][2]:
            image_index = 3
            print('The letter is: O')

        # U
        if lmList[8][2] < lmList[6][2] and lmList[12][2] < lmList[10][2] and lmList[16][2] > lmList[14][2] and \
                lmList[20][2] > lmList[18][2] and lmList[14][2] < lmList[4][2]:
            image_index = 4
            print('The letter is: U')

    if image_index < 5:
        image_to_show = overlayList[image_index]
        shape_img = image_to_show.shape
        img[0:shape_img[0], 0:shape_img[1]] = image_to_show

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (150, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow('image', img)
    cv2.waitKey(1)
