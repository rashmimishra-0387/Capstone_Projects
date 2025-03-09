import cv2
import mediapipe as mp

# Initialize MediaPipe Face Detection
mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Setup face detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.2)

# Initialize OpenCV to capture video from the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect faces
    results = face_detection.process(rgb_frame)

    # Draw face landmarks on the frame
    if results.detections:
        for detection in results.detections:
            # Draw bounding box around the detected face
            mp_drawing.draw_detection(frame, detection)

    # Display the resulting frame
    cv2.imshow("Face Detection", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
