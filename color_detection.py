import cv2
import numpy as np

def detect_color(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range untuk warna merah
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask_red1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])
    mask_red2 = cv2.inRange(hsv, lower_red2, upper_red2)

    red_mask = mask_red1 + mask_red2

    # Range untuk warna kuning
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    # Deteksi hasil
    if cv2.countNonZero(red_mask) > 500:
        color = "RED"
    elif cv2.countNonZero(yellow_mask) > 500:
        color = "YELLOW"
    else:
        color = "NONE"

    return color, red_mask, yellow_mask

def main():
    cap = cv2.VideoCapture(0)  # Webcam default

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        color, red_mask, yellow_mask = detect_color(frame)

        cv2.putText(frame, f"Color: {color}", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow("Webcam - Color Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
