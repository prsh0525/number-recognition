import tkinter as tk
from PIL import Image, ImageTk
import cv2
import mediapipe as mp

# Init
window = tk.Tk()
window.title('Sign Language Recognition')
window.geometry('1280x960')
window.resizable(False, False)

webcam_widget = tk.Label(window, width=1280, height=720)
text_widget = tk.Label(window, text='text')
graph_widget = tk.Label(window, text='graph')

# 위젯 배치
webcam_widget.grid(row=0, column=0, columnspan=5)
text_widget.grid(row=1, column=0)
graph_widget.grid(row=1, column=1, columnspan=4)

# Mediapipe
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands


def process():
    with mp_hands.Hands(model_complexity=0) as hands:
        # 손 인식
        image = cv2.flip(cap.read()[1], 1)
        results = hands.process(image)

        # 손이 있는 경우
        if results.multi_hand_landmarks:
            # 사진 위에 손 모양 그리기
            mp_drawing.draw_landmarks(
                image,
                results.multi_hand_landmarks[0],
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        # 결과 출력
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        tk_image = ImageTk.PhotoImage(image=Image.fromarray(image))

        webcam_widget.image = tk_image
        webcam_widget.configure(image=tk_image)

        # 50ms마다 새로고침
        window.after(10, process)


# Webcam
cap = cv2.VideoCapture(0)
process()

window.mainloop()
