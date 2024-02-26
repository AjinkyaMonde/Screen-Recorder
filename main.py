
import cv2
import pyautogui
import numpy as np

# Get the screen width and height
screen_width, screen_height = pyautogui.size()
dim = (screen_width, screen_height)

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('screen_recording.avi', fourcc, 20.0, dim)

try:
    while True:
        # Take a screenshot
        screenshot = pyautogui.screenshot()

        # Convert the screenshot to a numpy array
        frame = np.array(screenshot)

        # Convert the color of the frame to BGR
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        # Write the frame to the video file
        output.write(frame)

        # Break the loop when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    # Release the VideoWriter object when KeyboardInterrupt (e.g., Ctrl+C) occurs
    output.release()

# Release the VideoWriter object
output.release()
cv2.destroyAllWindows()

