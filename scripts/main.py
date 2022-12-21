import numpy as np
import mediapipe as mp
import cv2
from detecting0 import *
from detecting1 import *
from detecting_fist import * 
#создаем детектор
handsDetector = mp.solutions.hands.Hands()
cap = cv2.VideoCapture(0)
binary_number = ""
decimal_number = 0
prev_fist = False
i = 0
while(cap.isOpened()):
    i+=1
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q') or not ret:
        break
    flipped = np.fliplr(frame)
    # переводим его в формат RGB для распознавания
    flippedRGB = cv2.cvtColor(flipped, cv2.COLOR_BGR2RGB)
    # Распознаем
    results = handsDetector.process(flippedRGB)
    # Рисуем распознанное, если распозналось
    if results.multi_hand_landmarks is not None:
        (x, y), r = cv2.minEnclosingCircle(get_points(results.multi_hand_landmarks[0].landmark, flippedRGB.shape))
        ws = palm_size(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        #считаем отношения расстояний пальцев от концов до начала и от средней фаланги до начала
        t10 = distance8_50(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t20 = distance12_90(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t30 = distance16_130(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t40 = distance20_170(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t11 = distance8_51(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t21 = distance12_91(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t31 = distance16_131(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        t41 = distance20_171(results.multi_hand_landmarks[0].landmark, flippedRGB.shape)
        #проверяем сжат ли кулак
        if 2 * r / ws > 1.3:
             pass
        else:
             break
        #проверяем показана ли единица
        if t11 and t21 and t31 and t41:
            if i % 30 == 0:
                binary_number+="1"
            prev_fist = True
        else:
            if not prev_fist:
                prev_fist = True
        #проверяем показан ли ноль
        if t10 and t20 and t30 and t40:
            if i % 30 == 0:
                binary_number+="0"
            prev_fist = True
        else:
            if not prev_fist:
                prev_fist = True
    #переводим в десятичную
    if len(binary_number) > 0:
        decimal_number = int(binary_number, 2)
    strdec = "Decimal: " + str(decimal_number)
    strbin = "Binary: " + str(binary_number)
    # Рисуем наш результат в каждом кадре, даже если рука не детектировалась
    cv2.putText(flippedRGB, strdec, (10, 50), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 214, 120), thickness=2)
    cv2.putText(flippedRGB, strbin, (10, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 255, 255), thickness=1)
    # переводим в BGR и показываем результат
    res_image = cv2.cvtColor(flippedRGB, cv2.COLOR_RGB2BGR)
    cv2.imshow("Hands", res_image)
    #print(results.multi_handedness)

# освобождаем ресурсы
handsDetector.close()