import cv2
import numpy as np

## We will be working on dilation, erosion, opening, closing

## Dilation is the process of adding pixels to the boundaries of objects in an image
## Erosion is the process of removing pixels from the boundaries of objects in an image
## Opening is Erosion followed by Dilation :- Good for removing noise from the image
## Closing is Dilation followed by Erosion :- Good for removing noise from the image
## There are a lot other less famous morphological operations that can be researched
## Here, the objects must be white colored and background must be black colored
## If reverse of this is there, it will appear as if dilation is working as erosion (although actually, it's gonna be behaving as dilation only)

# Creating a sample image with black background and white colored text "Hello, World!" written on it
# This text will act as the object for morphological operations
black_img = np.zeros((600, 600), dtype=np.uint8)

# Placing the text on the image
cv2.putText(black_img, text="Hello, World!", org=(50, 300), fontFace=cv2.FONT_ITALIC, fontScale=2.5, color=255, thickness=3)
cv2.imshow("Original Image", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## So, morphological operations also use a kernel matrix (different than the one involved in blurring/sharpening)
## Here, the kernel matrix is nothing but a NxN matrix in which all elements are equal to 1

kernel_mat = np.ones((4, 4), dtype=np.uint8)

# Dilating the image
dilated_img = cv2.dilate(black_img, kernel=kernel_mat, iterations=1)

# Eroding the image
eroded_img = cv2.erode(black_img, kernel=kernel_mat, iterations=1)

# "Opening" the image
opened_img = cv2.morphologyEx(black_img, cv2.MORPH_OPEN, kernel=kernel_mat)

# "Closing the image"
closed_img = cv2.morphologyEx(black_img, cv2.MORPH_CLOSE, kernel=kernel_mat)

# Displaying the output images
cv2.imshow("Dilated Image", dilated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Eroded Image", eroded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Opened Image", opened_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Closed Image", closed_img)
cv2.waitKey(0)
cv2.destroyAllWindows()




