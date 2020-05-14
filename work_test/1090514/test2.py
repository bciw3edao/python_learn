import cv2

img = cv2.imread(r'../img/michaeljordan.jpg', cv2.IMREAD_GRAYSCALE)
# 黑白

img.fill(255)  # 加到全白
img.fill(256)  # 加到全黑

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
