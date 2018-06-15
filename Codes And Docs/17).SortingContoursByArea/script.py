import cv2
import numpy as np
import random

## Sorting contours help in eliminating noise while object recognition by removing the objects with smaller areas
## There are two ways to sort contours:-
## 1). Sorting by area helps in removing noise while object recognition and extract large contours
## 2). Sorting by spatial positions using the contour centroid. Here, the characters are sorted from left to right

def contour_areas (contours):
    cnt_areas = []
    for c in contours:
        cnt_areas.append(cv2.contourArea(c))
    return cnt_areas

# Creating black colored RGB canvases of the resolution 512x512
black_img = np.zeros((512, 512, 3), dtype=np.uint8)

# Creating some shapes in the canvas
cv2.rectangle(black_img, (50, 200), (250, 350), color=(255, 255, 255), thickness=-1)
cv2.rectangle(black_img, (100, 250), (200, 300), color=(0, 0, 0), thickness=-1)
cv2.rectangle(black_img, (300, 200), (450, 350), color=(255, 255, 255), thickness=-1)

sample_img = cv2.cvtColor(black_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

canny_edged_img = cv2.Canny(sample_img, threshold1=50, threshold2=255)
cv2.imshow("Edged image", canny_edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, contours, hierarchy = cv2.findContours(sample_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# printing the list of contours
print (contour_areas(contours))

# Contours sorted from small to large contours
sorted_contours = sorted(contours, key=lambda x: cv2.contourArea(x))

# Printing the sorted contour areas
print(contour_areas(sorted_contours))

# Drawing each contour at time
for (index, contour) in enumerate(sorted_contours):
    cv2.drawContours(black_img, [contour], -1, color=(0, 50*index, 255), thickness=2)

# Displaying the final image with differently colored contours
cv2.imshow("Final image with sorted contours", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

