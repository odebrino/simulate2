import cv2
import mediapipe as mp
import os

# Mediapipe setup
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Path to test images
data_path = os.path.expanduser("~/simulate2/data")

# Load the model
with mp_hands.Hands(static_image_mode=True, max_num_hands=2, min_detection_confidence=0.5) as hands:
    for fname in os.listdir(data_path):
        if fname.lower().endswith((".jpg", ".png", ".jpeg")):
            img_path = os.path.join(data_path, fname)
            image = cv2.imread(img_path)
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Process
            result = hands.process(rgb)

            # Draw landmarks
            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Show result
            cv2.imshow("Hand Tracking", image)
            cv2.waitKey(0)

cv2.destroyAllWindows()
