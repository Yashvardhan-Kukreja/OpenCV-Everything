import cv2
import numpy as np

## Segmentation is the process of dividing an image into different regions
## Contours are lines or curves that bound the cover of an object in an image

# Creating black colored RGB canvases of the resolution 512x512
black_img = np.zeros((512, 512, 3), dtype=np.uint8)
black_img_1 = np.zeros((512, 512, 3), dtype=np.uint8)

# Creating some shapes in the canvas
cv2.rectangle(black_img, (50, 200), (250, 350), color=(255, 255, 255), thickness=-1)
cv2.rectangle(black_img, (100, 250), (200, 300), color=(0, 0, 0), thickness=-1)
cv2.rectangle(black_img, (300, 200), (450, 350), color=(255, 255, 255), thickness=-1)

cv2.rectangle(black_img_1, (50, 200), (250, 350), color=(255, 255, 255), thickness=-1)
cv2.rectangle(black_img_1, (100, 250), (200, 300), color=(0, 0, 0), thickness=-1)
cv2.rectangle(black_img_1, (300, 200), (450, 350), color=(255, 255, 255), thickness=-1)

sample_img = cv2.cvtColor(black_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

canny_edged_img = cv2.Canny(sample_img, threshold1=50, threshold2=255)
canny_edged_img_1 = canny_edged_img
cv2.imshow("Edged image", canny_edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## CHAIN_APPROX_NONE stores all the bounding points. This mode is good when the image is pretty complex
## But in this case, the shapes in the image are just simple boxes and instead of needing all the bouding points
## , things can be worked by just the end points of the shapes
## So, we will be using CHAIN_APPROX_SIMPLE method which returns just the end points instead of all the bounding points thereby, making the program more efficient

ret, contours, hierarchy = cv2.findContours(canny_edged_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
ret_1, contours_1, hierarchy_1 = cv2.findContours(canny_edged_img_1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

## Now, the RETR_EXTERNAL contour mode returns only outer/external contours
## While, the RETR_LIST contour mode returns all the inner and outer contours
## Also, the RETR_TREE contour mdoe returns all the contours in full hierarchy
## Hierarchy is a pretty lengthy concept so, the main documentation will help more regarding that

# Printing the number of contours in each case
print("Number of contours with RETR_EXTERNAL contour mode: ", len(contours))
print("Number of contours with RETR_LIST contour mode: ", len(contours_1))

# Drawing lines on the contours in the image
cv2.drawContours(black_img, contours, -1, (255, 0, 0), thickness=2)
cv2.drawContours(black_img_1, contours_1, -1, (255, 0, 0), thickness=2)

# Printing the final images
cv2.imshow("Final image (mode :- RETR_EXTERNAL) with contours", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("Final image (mode :- RETR_LIST) with contours", black_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()