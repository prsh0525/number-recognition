import tkinter as tk
from PIL import Image, ImageTk
import cv2

# Init
window = tk.Tk()
window.title('Sign Language Recognition')
window.geometry('1600x800')
window.resizable(False, False)

webcam_widget = tk.Label(window, text='webcam')
hand_widget = tk.Label(window, text='hand')
text_widget = tk.Label(window, text='text')
graph_widget = tk.Label(window, text='graph')

# 위젯 배치
webcam_widget.grid(row=0, column=0, rowspan=2)
hand_widget.grid(row=0, column=1)
text_widget.grid(row=1, column=1)
graph_widget.grid(row=2, column=0, columnspan=2)


def show_frames():
    frame = cv2.flip(cap.read()[1], 1)
    cv2_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    raw_image = Image.fromarray(cv2_image)
    tk_image = ImageTk.PhotoImage(image=raw_image)

    webcam_widget.image = tk_image
    webcam_widget.configure(image=tk_image)

    # 20ms마다 새로고침
    window.after(20, show_frames)


# Webcam
cap = cv2.VideoCapture(0)
show_frames()

window.mainloop()
