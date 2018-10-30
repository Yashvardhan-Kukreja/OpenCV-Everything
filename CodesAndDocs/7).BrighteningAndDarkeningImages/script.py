import cv2
import numpy as np

sample_img = cv2.imread("../sample.png")

# the variable "factor" will determine the intensity of darkness or lightness of the image
# More the value of the variable factor , more the intensity of the darkness or the lightness of the image
factor = 75
dark_bright_matrix = np.ones(sample_img.shape, dtype=np.uint8) * factor

# Original Image
cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)

# Making the image brighter
brighter_img = cv2.add(sample_img, dark_bright_matrix)
cv2.imshow("Brighter image", brighter_img)
cv2.waitKey(0)

# Making the image darker
dark_img = cv2.subtract(sample_img, dark_bright_matrix)
cv2.imshow("Darker Image", dark_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

