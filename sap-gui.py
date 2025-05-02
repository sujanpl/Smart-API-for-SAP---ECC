import pyautogui
import subprocess
import time

# Function to type text slowly
def type_text(text):
    pyautogui.typewrite(text, interval=0.1)

# Function to wait until a pixel color changes (meaning screen has changed)
def wait_for_screen_change(x, y, timeout=60):
    initial_color = pyautogui.screenshot().getpixel((x, y))
    start_time = time.time()
    
    while True:
        current_color = pyautogui.screenshot().getpixel((x, y))
        if current_color != initial_color:
            print("Screen change detected!")
            return True
        if (time.time() - start_time) > timeout:
            print("Timeout reached. No screen change detected.")
            return False
        time.sleep(1)

# Billing date range
from_date = input("Enter FROM Billing Date (DD.MM.YYYY): ")
to_date = input("Enter TO Billing Date (DD.MM.YYYY): ")

# Start SAP Logon GUI
subprocess.Popen(r"C:\Program Files (x86)\SAP\FrontEnd\SAPgui\saplogon.exe")         
time.sleep(5)

# Navigate to the "1.1 LV Production System" connection
time.sleep(2)
type_text("1.1 LV Production System - ECC")  
pyautogui.press("enter")  
time.sleep(5)

# Log in to SAP
type_text("VSK001")  # Username
pyautogui.press("tab")
time.sleep(2)

type_text("DAIPL@2025")
time.sleep(2)

pyautogui.press("enter")    
time.sleep(2)

# Enter the transaction code
type_text("ZSDR22")  
pyautogui.press("enter")
time.sleep(2)  

# Fill in the fields
type_text("5000")  
pyautogui.press("tab")
time.sleep(2)

# Plant
type_text("1005")
pyautogui.press("tab")
time.sleep(0.2)

# Tab actions
pyautogui.press("tab")
time.sleep(0.2)
pyautogui.press("tab")
time.sleep(0.2)

# Billing date from and to
type_text(from_date)  
pyautogui.press("tab")
time.sleep(1)

type_text(to_date)      
time.sleep(1)

pyautogui.press("f8")
time.sleep(5)  # Increased wait time after F8

# Wait for SAP screen to change after F8
if wait_for_screen_change(x=300, y=400):  # Adjust coordinates as needed
    time.sleep(2)  # Additional wait for elements to load

    # Check for specific UI element (e.g., layout button)
    layout_button_location = pyautogui.locateOnScreen('layout_button_image.png', confidence=0.8)
    if layout_button_location:
        pyautogui.click(layout_button_location)  # Click the layout button
        time.sleep(1)  # Wait for the layout options to load
        pyautogui.hotkey("ctrl", "f9")  # Perform Ctrl + F9
        print("Ctrl + F9 action performed successfully.")
    else:
        print("Layout button not found. Please check the screen.")
else:
    print("Screen change not detected. Please check the process.")
