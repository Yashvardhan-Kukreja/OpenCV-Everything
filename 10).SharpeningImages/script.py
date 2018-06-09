import cv2
import numpy as np

sample_img = cv2.imread("../sample.png")

cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Here also, we use the method of kernel matrix
## The only difference is that here, all the elements of the kernel matrix are -1 except the middlemost elementof the matrix
## The middlemost element = 1 + sum of all the other elements
## Thereby, maintaining the sum of all elements in the kernel matrix = 1

kernel_mat = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]], dtype=np.float32)

sharpened_img = cv2.filter2D(sample_img, -1, kernel_mat)

cv2.imshow("Sharpened Image", sharpened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()