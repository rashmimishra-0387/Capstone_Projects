#pip install mediapipe opencv-python
import cv2
import mediapipe as mp

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

# Initialize the webcam
cap = cv2.VideoCapture(0)

def count_fingers(hand_landmarks):
    # Define the indices of the landmarks for each finger (thumb, index, middle, ring, pinky)
    # These are the landmark indices in MediaPipe for the open/close finger detection
    thumb_tip = hand_landmarks.landmark[4]
    index_tip = hand_landmarks.landmark[8]
    middle_tip = hand_landmarks.landmark[12]
    ring_tip = hand_landmarks.landmark[16]
    pinky_tip = hand_landmarks.landmark[20]

    # Count how many fingers are open
    open_fingers = 0

    # Thumb: Check if thumb is open (check if thumb tip is right of the thumb base)
    if thumb_tip.x > hand_landmarks.landmark[3].x:
        open_fingers += 1

    # Index finger: Check if index finger is open (check if index tip is above the index base)
    if index_tip.y < hand_landmarks.landmark[7].y:
        open_fingers += 1

    # Middle finger: Check if middle finger is open (check if middle tip is above the middle base)
    if middle_tip.y < hand_landmarks.landmark[11].y:
        open_fingers += 1

    # Ring finger: Check if ring finger is open (check if ring tip is above the ring base)
    if ring_tip.y < hand_landmarks.landmark[15].y:
        open_fingers += 1

    # Pinky finger: Check if pinky finger is open (check if pinky tip is above the pinky base)
    if pinky_tip.y < hand_landmarks.landmark[19].y:
        open_fingers += 1

    return open_fingers

while True:
    # Capture frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to RGB (MediaPipe works with RGB images)
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Hands to detect hand landmarks
    results = hands.process(frame_rgb)

    if results.multi_hand_landmarks:
        # For each hand detected, draw landmarks and count fingers
        for landmarks in results.multi_hand_landmarks:
            # Draw landmarks on the hand
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Count the number of fingers that are open
            num_fingers = count_fingers(landmarks)
            # Display the number of fingers on the frame
            cv2.putText(frame, f'Fingers Open: {num_fingers}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the resulting frame with hand landmarks and finger count
    cv2.imshow('Hand Detection and Finger Count', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
