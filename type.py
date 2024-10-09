import pytesseract
import pyautogui
from PIL import Image
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
tesseract_path = os.path.join(current_dir, 'tesseract', 'tesseract.exe')

pytesseract.pytesseract.tesseract_cmd = tesseract_path

filename = input("Enter the file name: ")
time.sleep(5)
image = Image.open(filename)

text = pytesseract.image_to_string(image)

for line in text.splitlines():
    if line.strip():
        pyautogui.write(line, interval=0.000000000001)
    pyautogui.press('space')
