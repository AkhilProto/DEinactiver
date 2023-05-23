import pyautogui
import time

def prevent_inactivity():
    screen_width, screen_height = pyautogui.size()
    corner_threshold = 10  # Number of pixels near the corner to trigger adjustment

    while True:
        x, y = pyautogui.position()
        
        # Check if cursor is near the corners
        if x <= corner_threshold:
            x += 10  # Move 10 pixels to the right
        elif x >= screen_width - corner_threshold:
            x -= 10  # Move 10 pixels to the left

        if y <= corner_threshold:
            y += 10  # Move 10 pixels down
        elif y >= screen_height - corner_threshold:
            y -= 10  # Move 10 pixels up
        
        pyautogui.moveTo((x+6), (y+6), duration=0.1)  # Move the mouse to the adjusted position
        time.sleep(0.5)
        pyautogui.moveTo((x-6), (y-6), duration=0.1) 
        time.sleep(5)  # Wait for 5 seconds before moving again

# Call the function to start preventing inactivity
prevent_inactivity()
