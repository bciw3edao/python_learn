import cv2
import numpy as np

img = cv2.imread(r'../img/tooDark.jpg', cv2.IMREAD_GRAYSCALE)
# 黑白

newImage = np.log10(img) * 100
print(newImage.dtype)

newImage = newImage.astype(np.uint8)
cv2.imshow('new Image', newImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
