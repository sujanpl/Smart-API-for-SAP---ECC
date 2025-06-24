import pyautogui
import subprocess
import time

# Function to type text slowly
def type_text(text):
    pyautogui.typewrite(text, interval=0.1)

# Enter the Billing Date range.
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
 

# Log in to SAP ECC system

type_text("XYZ")  # Username
pyautogui.press("tab")
time.sleep(2)

 #password
type_text("ABCD")
time.sleep(25)  # Wait for the data to load after execution

#action to save the present layout data
pyautogui.hotkey('ctrl', 'shift', 'f9')

time.sleep(5)

#action for arrow down
pyautogui.press('down')
time.sleep(2)
pyautogui.press("enter")    
time.sleep(3)

#action for arrow up
pyautogui.press('up')
#select the present file path
pyautogui.hotkey('ctrl','a')
time.sleep(1)
#delet the file path 
pyautogui.press('backspace')

#write the new path file
type_text(r'C:\Users\malikjan.mujawar\Desktop')
pyautogui.press("tab")

#write file name
type_text('SAP-DATA2.xls')
time.sleep(1)
pyautogui.press("enter")    
print("Export process initiated successfully.")
