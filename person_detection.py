import cv2
from ultralytics import YOLO
import pygame
import threading
import XInput 
import time

pygame.mixer.init()

model = YOLO('C:/Users/Colton/runs/detect/train8/weights/best.pt')  

cap = cv2.VideoCapture(0)

class_names = ['drowsy']

audio_file = 'Alert (1 time).mp3'

def play_alert_sound_with_vibration():
    """Play the alert sound and activate vibration for the duration of the sound."""
    pygame.mixer.music.load(audio_file)
    sound_length = pygame.mixer.Sound(audio_file).get_length()

    pygame.mixer.music.play()

    XInput.set_vibration(0, 1.0, 1.0)  
    time.sleep(sound_length)          
    XInput.set_vibration(0, 0.0, 0.0) 
alert_playing = False

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    alert_detected = False 

    for result in results:
        boxes = result.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            if 0 <= cls_id < len(class_names):
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                label = f"{class_names[cls_id]}: {conf * 100:.2f}%"

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame, label, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2
                )

                if class_names[cls_id] == 'drowsy' and conf < 0.3:
                    alert_detected = True

    if alert_detected and not alert_playing:
        alert_playing = True
        threading.Thread(target=play_alert_sound_with_vibration, daemon=True).start()

    if not alert_detected and alert_playing and not pygame.mixer.music.get_busy():
        alert_playing = False

    cv2.imshow("Drowsiness Detection", frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
