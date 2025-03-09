import cv2
import mediapipe as mp

# Initialize MediaPipe Pose Estimation
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Setup Pose Estimation
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Initialize OpenCV to capture video from the webcam
cap = cv2.VideoCapture(0)

def check_namaskara_pose(landmarks):
    # Checking the positions of the hands and elbows to detect Namaskara pose
    try:
        # Define landmarks for the left and right hands and elbows
        left_wrist = landmarks[mp_pose.PoseLandmark.LEFT_WRIST]
        right_wrist = landmarks[mp_pose.PoseLandmark.RIGHT_WRIST]
        left_elbow = landmarks[mp_pose.PoseLandmark.LEFT_ELBOW]
        right_elbow = landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW]
        
        # Check if wrists are near each other (distance between left and right wrists should be small)
        distance = ((left_wrist.x - right_wrist.x)**2 + (left_wrist.y - right_wrist.y)**2)**0.5

        # If distance between wrists is small and elbows are slightly bent
        if distance < 0.2 and abs(left_elbow.y - right_elbow.y) < 0.1:
            return True
        return False
    except:
        return False

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert the BGR image to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame and detect the pose landmarks
    results = pose.process(rgb_frame)

    # Draw pose landmarks on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Check if Namaskara pose is detected
        if check_namaskara_pose(results.pose_landmarks.landmark):
            cv2.putText(frame, "Namaskara Pose Detected!", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Namaskara Pose Not Detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow("Pose Estimation", frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close the OpenCV window
cap.release()
cv2.destroyAllWindows()
