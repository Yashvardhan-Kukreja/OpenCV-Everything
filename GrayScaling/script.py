import cv2

sample_img = cv2.imread("../sample.png")

# Converting the sample_img to grayscale
grayscale_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)

# Displaying the original and grayscaled image
cv2.imshow("Original Image", sample_img)
cv2.imshow("Grayscaled Image", grayscale_img)

# Closing the currently launched image windows
cv2.waitKey(0)
cv2.destroyAllWindows()

#
##
### OR OR OR The GrayScaled image can be loaded directly with a shorter method given below
##
#

sample_grayscale_img = cv2.imread("../sample.png", 0)
cv2.imshow("Direct Grayscaled Image", sample_grayscale_img)

cv2.waitKey(0)
cv2.destroyAllWindows()