import cv2
import numpy as np

# ============================================================
# >>> EDIT THIS BEFORE RUNNING <
# ============================================================
CAMERA_URL = "http://10.110.3.101.8080/video   # <-- CHANGE to YOUR phone's IP Webcam address
# ============================================================

cap = cv2.VideoCapture(CAMERA_URL)

def nothing(x):
    pass

cv2.namedWindow("Control Panel")
cv2.createTrackbar("L-H", "Control Panel", 0, 179, nothing)
cv2.createTrackbar("L-S", "Control Panel", 0, 255, nothing)
cv2.createTrackbar("L-V", "Control Panel", 0, 255, nothing)
cv2.createTrackbar("U-H", "Control Panel", 179, 179, nothing)
cv2.createTrackbar("U-S", "Control Panel", 255, 255, nothing)
cv2.createTrackbar("U-V", "Control Panel", 255, 255, nothing)

saved_lower = None
saved_upper = None

print("Adjust sliders until only your marker shows white in the Mask.")
print("Press 's' to SAVE values.  Press 'q' to QUIT.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No frame received")
        break

    frame = cv2.resize(frame, (400, 300))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H", "Control Panel")
    l_s = cv2.getTrackbarPos("L-S", "Control Panel")
    l_v = cv2.getTrackbarPos("L-V", "Control Panel")
    u_h = cv2.getTrackbarPos("U-H", "Control Panel")
    u_s = cv2.getTrackbarPos("U-S", "Control Panel")
    u_v = cv2.getTrackbarPos("U-V", "Control Panel")

    lower = np.array([l_h, l_s, l_v])
    upper = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(frame, frame, mask=mask)
    mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

    cv2.putText(frame, "Camera Feed", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    cv2.putText(mask_bgr, "Mask", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(result, "Result", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    status = "SAVED" if saved_lower is not None else "Press 's' to save"
    blank = np.zeros_like(frame)
    cv2.putText(blank, status, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    cv2.putText(blank, "Press 'q' to quit", (10, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 1)

    top_row = np.hstack((frame, mask_bgr))
    bottom_row = np.hstack((result, blank))
    grid = np.vstack((top_row, bottom_row))

    cv2.imshow("Control Panel", grid)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('s'):
        saved_lower = (l_h, l_s, l_v)
        saved_upper = (u_h, u_s, u_v)
        print()
        print("================================")
        print(" VALUES SAVED — copy this into")
        print(" your main OpenCV code:")
        print("================================")
        print(f"LOWER_COLOR = np.array([{l_h}, {l_s}, {l_v}])")
        print(f"UPPER_COLOR = np.array([{u_h}, {u_s}, {u_v}])")
        print("================================")

    if key == ord('q'):
        if saved_lower is None:
            print()
            print("(No values were saved with 's' — using last slider position)")
            print(f"LOWER_COLOR = np.array([{l_h}, {l_s}, {l_v}])")
            print(f"UPPER_COLOR = np.array([{u_h}, {u_s}, {u_v}])")
        break

cap.release()
cv2.destroyAllWindows() what would be file name for this in github
