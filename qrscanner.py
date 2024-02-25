import cv2

camera_id = 0
delay = 1
window_name = 'OpenCV QR Code'
qcd = cv2.QRCodeDetector()
cap = cv2.VideoCapture(camera_id)
ret, frame = cap.read()
    
def qr_detect():
    ret, frame = cap.read()
    if ret:
        retval, points, straight_code = qcd.detectAndDecode(frame)
        return retval
    else:
        return ""
    
def open_window():
    ret, frame = cap.read()
    if ret:
        cv2.imshow(window_name, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return 0
    
def destroy_windows():
    cv2.destroyAllWindows()