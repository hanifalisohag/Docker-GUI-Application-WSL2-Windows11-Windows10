import cv2

img = cv2.imread('hanif.jpg',1)
cv2.imshow('Docker GUI Demo Hanif',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
