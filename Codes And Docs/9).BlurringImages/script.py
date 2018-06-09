import cv2
import numpy as np

## So, blurring happens in an image  when we average pixels within a region
## The larger that region, the more  the blur effect
## That region is called kernel.
## So, we give the image an input called kernel_matrix which is square matrix leading to some of all of its elements = 1
## The larger that matrix is, the more the image will be blurred
## This method of blurring an image using kernel matrix is called convolution

# Here, let's create a 10x10 kernel matrix

sample_img = cv2.imread("../sample.png")
cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

kernel_mat = np.ones((10, 10), dtype=np.float32)*(1/100)
## The multiplication with (1/100) normalises that kernel_mat, so that the sum of all of its elements becomes equal to 1

# Creating the blurred image of the sample image using cv2.filter2D function
blurred_img = cv2.filter2D(sample_img, -1, kernel_mat)
cv2.imshow("Blurred Image", blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Other readymade methods to blur an image are given below

# Box Blur (Same as the blurring method we used above)
## Uses average of all the elements in kernel region
box_blurred_img = cv2.blur(sample_img, (7, 7))
cv2.imshow("Box Blurred Image", box_blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Gaussian Blur
## Uses Gaussian Kernel instead of normal averaging kernel
gaussian_blurred_img = cv2.GaussianBlur(sample_img, (7, 7), 0)
cv2.imshow("Gaussian Blurred Image", gaussian_blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Median Blur
## Uses median of all the elements in kernel region
median_blurred_img = cv2.medianBlur(sample_img, 7)
cv2.imshow("Median Blurred Image", median_blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Bilateral filtering :- Commonly used as a noise removal technique
## Blurs while keeping the edges sharp
## Takes two GaussianFilters to produce a function of pixel difference
## This pixel difference function makes sure only those pixels with similar intensity to that of central pixel are considered for blurring
## Hence, this preserves the edges since pixels at edges have large intensity variations
bilateral_blurred_img = cv2.bilateralFilter(sample_img, 9, 100, 100)
cv2.imshow("Bilateral Blurred Image", bilateral_blurred_img)
cv2.waitKey(0)
cv2.destroyAllWindows()