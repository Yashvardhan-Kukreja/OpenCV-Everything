import cv2
import numpy as np

sample_img = cv2.imread("../sample.png")
cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Thresholding is an operation which converts some parts of an image into plain black and other parts into plain white
## Basically, while using this functionality, we provide two pixel values, one min and one max.
## Then, in the whole image, each pixel is compared with these two values and if a pixel's value lies between these two threshold values, then that pixel value is converted to the max value otherwise it's converted to 0 i.e. black
## Thresholding is usually applied on grayscale images because the output image doesn't need any colors

## So, here, let's consider the max value for thresholding = 200
## And let's consider the threshold (min) value for thresholding = 100
## So now, any pixel value between 100 and 200 will be changed to 200
## And, any pixel value < 100 or > 200 will be changed to 0 thereby, making it a black pixel

greyscale_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Greyscaled Image", greyscale_img)
cv2.waitKey(0)

max_val = 200
thresh_val = 100

## When the thresholding type = cv2.THRESH_BINARY or cv2.THRESH_BINARY_INV, then it is called Binarization
## cv2.threshold function returns an array containing two elements. The second element is the thresholded image
ret, thresholded_img = cv2.threshold(greyscale_img, thresh_val, max_val, cv2.THRESH_BINARY)
### OR
thresholded_img = cv2.threshold(greyscale_img, thresh_val, max_val, cv2.THRESH_BINARY)[1]
cv2.imshow("Thresholded Image", thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## When the threshold type = cv2.THRESH_BINARY_INV, then the final image is inverse of the one with type cv2.THRESH_BINARY
ret, thresholded_img_inv = cv2.threshold(greyscale_img, thresh_val, max_val, cv2.THRESH_BINARY_INV)
### OR
thresholded_img_inv = cv2.threshold(greyscale_img, thresh_val, max_val, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Thresholded Image Inverse", thresholded_img_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()

## TODO: I will be adding the details and code about other Thresholding types soon
## TODO: Will be adding adaptive thresholding as well

