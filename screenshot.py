import time
import pyautogui
import tkinter as tk

def screenshot():
    name = int(round(time.time() * 1000))
    name = 'D:/screenshots/{}.png'.format(name)
    image = pyautogui.screenshot(name)
    image.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(
    frame,
    text = "New Screenshot",
    command = screenshot)
button.pack(side-tk.LEFT)

close = tk.Button(
    frame,
    text = "Exit",
    command = quit)
close.pack(side-tk.LEFT)

root.mainloop()
