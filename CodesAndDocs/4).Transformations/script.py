import cv2
import numpy as np

## There two types of transformations Affine and Non-Affine
## In Affine transformations, the uniformity, the parallelness and the angles between the sides of the shape are preserved
## For example, a square will still remain a square after an Affine transformation despite its area may increase or decrease or it gets rotated
## Usually, affine transformations include rotating the shape or translating the shape

## Now, in Non-Affine transformations, no uniformity is maintained in the shape
## For example, a square might get converted to a trapezium or an irregular quadrilateral after a Non-Affine transformation

sample_img = cv2.imread("../sample.png")

# Extracting the shape of the image
height, width = sample_img.shape[:2]

### Affine transformations:

## 1). Translating the image
# Calculating the translation matrix
trans_mat = np.array([[1, 0, height/5], [0, 1, width/5]], dtype=np.float32)

# Creating the translated image corresponding to the translation matrix
translated_img = cv2.warpAffine(sample_img, trans_mat, (height, width))

cv2.imshow("Translated image", translated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 2). Rotating the image
# We will rotate the image by 60 degrees
# Calculating the rotational matrix
rotation_mat = cv2.getRotationMatrix2D(center=(height/2, width/2), angle=60, scale=0.75)

# Creating the rotated image corresponding to the rotational matrix
rotated_img = cv2.warpAffine(sample_img, rotation_mat, (height, width))

cv2.imshow("Rotated image", rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## 3). Flipping the image horizontally
## This is same as rotating the image by 90 degrees but with a shorter method (in just one line)
flipped_img = cv2.transpose(sample_img)

cv2.imshow("Flipped image", flipped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
