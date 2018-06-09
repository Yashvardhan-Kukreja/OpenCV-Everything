import cv2

sample_img = cv2.imread("../sample.png")

## Usually, in openCV there's no need to use fully colored images to apply different kinds of operations
## The desirable can be achieved by using a greyscaled image of the input image
## By using greyscaled image instead of colored, efficiency and the speed of the process is way more increased
## Because instead of using three RGB components of a pixel in a colored image, only one component of a pixel in a greyscale image will be used for calculations
## Thereby, reducing the time complexity of the program a lot

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