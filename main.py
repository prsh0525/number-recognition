import tkinter as tk
from PIL import Image, ImageTk
import cv2

# Init
window = tk.Tk()
window.geometry('1600x800')
window.resizable(False, False)

webcam_widget = tk.Label(window, text='webcam').grid(row=0, column=0)
hand_widget = tk.Label(window, text='hand').grid(row=0, column=1)
graph_widget = tk.Label(window, text='graph').grid(row=1, column=0)
text_widget = tk.Label(window, text='text').grid(row=1, column=1)

window.mainloop()
