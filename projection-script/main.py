import pygetwindow as gw
import pyautogui
from PIL import ImageGrab
import cv2
import numpy as np

# Get the Unity game window by title (replace with the title of the Unity window)
window_title = "Unity Hub 3.9.1"  # Replace with the actual title of the Unity game window
window = gw.getWindowsWithTitle(window_title)

if not window:
    print(f"Window titled '{window_title}' not found.")
    exit()

win = window[0]

# Screen size of the secondary monitor (adjust to your secondary monitor resolution)
secondary_screen_width = 1920  # Replace with your secondary monitor width
secondary_screen_height = 1080  # Replace with your secondary monitor height

# Continuously capture the Unity game window and display it on the secondary screen
while True:
    # Bring the game window to the front
    win.activate()

    # Get the window's position and size
    left, top, right, bottom = win.left, win.top, win.right, win.bottom

    # Capture the screenshot of the game window area
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Convert the screenshot to an OpenCV image (NumPy array)
    img = np.array(screenshot)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    # Resize the image to fit the secondary screen resolution
    resized_img = cv2.resize(img, (secondary_screen_width, secondary_screen_height))

    # Display the captured image in a full-screen window on the secondary screen
    cv2.namedWindow("Projected Game", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Projected Game", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Projected Game", resized_img)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cv2.destroyAllWindows()
