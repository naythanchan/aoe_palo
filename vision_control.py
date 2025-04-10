import cv2

# Try different indexes if needed (0, 1, 2...)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't access camera.")
        break

    cv2.imshow("Camo Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
