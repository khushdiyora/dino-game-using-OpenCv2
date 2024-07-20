import cv2
import cvzone
from cvzone.HandTrackingModule import HandDetector
import pyautogui as auto

# Initialize the webcam and hand detector
cap = cv2.VideoCapture(0)
hd = HandDetector(maxHands=1)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (1080, 720))
    cvzone.putTextRect(frame, 'DINO GAME GESTURE', [360, 40], scale=3, thickness=3, border=2, colorT=(135, 206, 235))  # Sky blue color

    # Detect hands in the frame
    hand, frame = hd.findHands(frame)
    
    if hand:
        hands = hand[0]
        lmList = hands['lmList']

        # Draw smaller green circles on all landmarks
        for lm in lmList:
            cv2.circle(frame, tuple(lm[:2]), 8, (0, 255, 0), cv2.FILLED)  # Smaller green circles

        # Get the positions of the thumb and index finger tips
        thumb_tip = lmList[4][0:2]
        index_tip = lmList[8][0:2]

    

        # Calculate the distance between the thumb and index finger tips
        length, info, frame = hd.findDistance(thumb_tip, index_tip, frame)
        length = round(length)

        # Trigger the up arrow key press if the distance is less than 25
        if length < 25:
            auto.press('up')

    # Display the frame
    cv2.imshow('Dino Game using finger gesture', frame)
    
    # Break the loop if 'p' is pressed
    if cv2.waitKey(1) == ord('p'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
