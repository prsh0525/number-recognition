import tkinter as tk
from PIL import Image, ImageTk

import cv2
import mediapipe as mp
import joblib

# tkinter init
window = tk.Tk()
window.title('Number Recognition')
window.geometry('1280x880')
window.resizable(False, False)

webcam_widget = tk.Label(window, width=1280, height=720)
result_widget = tk.Label(window, text='인식 결과', font=('Helvetica Bold', 64))

# 위젯 배치
webcam_widget.grid(row=0, column=0)
result_widget.grid(row=1, column=0, padx=32, pady=32)

# Mediapipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# 모델 불러오기
model = joblib.load('model/hand_model.pkl')


def main():
    image = cv2.cvtColor(cv2.flip(cap.read()[1], 1), cv2.COLOR_BGR2RGB)

    with mp_hands.Hands(static_image_mode=True) as hands:
        results = hands.process(image)

        # 손이 있는 경우
        if results.multi_hand_landmarks:
            # landmark 그리기
            mp_drawing.draw_landmarks(
                image,
                results.multi_hand_landmarks[0],
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style(),
            )

            # 모델에 전달하기 위해 전처리
            coordinate = []
            landmark = results.multi_hand_landmarks[0].landmark
            for n in range(21):
                coordinate.extend([landmark[n].x, landmark[n].y])

            # 결과 출력
            prediction = model.predict([coordinate])
            result_widget.config(text=f'결과: {prediction[0]}')

    tk_image = ImageTk.PhotoImage(image=Image.fromarray(image))
    webcam_widget.image = tk_image
    webcam_widget.configure(image=tk_image)

    # 10ms마다 새로고침
    window.after(10, main)


# Webcam
cap = cv2.VideoCapture(0)
main()

window.mainloop()
