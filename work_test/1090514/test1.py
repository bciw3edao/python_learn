import cv2

img = cv2.imread(r'../img/michaeljordan.jpg', cv2.IMREAD_GRAYSCALE)

print(type(img))
print(img.dtype)
print(img.ndim)
print(img.shape)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
