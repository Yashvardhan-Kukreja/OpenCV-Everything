import cv2
import numpy as np

black_img_1 = np.zeros((400, 400), dtype=np.uint8)
black_img_2 = np.zeros((400, 400), dtype=np.uint8)

cv2.imshow("Original Image", black_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adding a white colored square to first image
cv2.rectangle(black_img_1, (100, 100), (300, 300), color=255, thickness=-1)

cv2.imshow("Image 1", black_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adding a white colored circle to second image
cv2.circle(black_img_2, (300, 250), radius=95, color=255, thickness=-1)

cv2.imshow("Image 2", black_img_2)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Imposing both the images on each other with respective bitwise operations i.e. OR, AND, NOT, XOR

# Imposing using AND operation
# Final image will have only that portion white where both images are white at a time
and_output = cv2.bitwise_and(black_img_1, black_img_2)
cv2.imshow("Images imposed with AND operation", and_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imposing using OR operation
# Final image will have only that portion white where any of the two images are white
or_output = cv2.bitwise_or(black_img_1, black_img_2)
cv2.imshow("Images imposed with OR operation", or_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Imposing using XOR operation
# Final image will have only that portion white where both images will have opposite colors
xor_output = cv2.bitwise_xor(black_img_1, black_img_2)
cv2.imshow("Images imposed with XOR operation", xor_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying NOT operation on both of the images
# Final image will be inverted of the original image
not_output_1 = cv2.bitwise_not(black_img_1)
cv2.imshow("Image 1 with NOT operation", not_output_1)
cv2.waitKey(0)
cv2.destroyAllWindows()

not_output_2 = cv2.bitwise_not(black_img_2)
cv2.imshow("Image 2 with NOT operation", not_output_2)
cv2.waitKey(0)
cv2.destroyAllWindows()



