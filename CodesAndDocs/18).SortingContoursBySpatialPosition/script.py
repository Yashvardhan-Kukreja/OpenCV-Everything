import cv2
import numpy as np

def x_cord_of_contour(contour):
    moment_mat = cv2.moments(contour)
    return int(moment_mat['m10']/moment_mat['m00'])

def y_cord_of_contour(contour):
    moment_mat = cv2.moments(contour)
    return int(moment_mat['m01']/moment_mat['m00'])


def label_contour_center(image, contour, label):
    cx = x_cord_of_contour(contour)
    cy = y_cord_of_contour(contour)
    cv2.circle(image, (cx, cy), 5, color=(0, 255, 0), thickness=-1)
    cv2.putText(image, str(label), (cx, cy), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)
    return image

# Creating black colored RGB canvases of the resolution 512x512
black_img = np.zeros((512, 512, 3), dtype=np.uint8)

# Creating some shapes in the canvas
cv2.rectangle(black_img, (50, 200), (250, 350), color=(255, 255, 255), thickness=-1)
cv2.rectangle(black_img, (75, 225), (175, 300), color=(0, 0, 0), thickness=-1)
cv2.rectangle(black_img, (300, 200), (450, 350), color=(255, 255, 255), thickness=-1)

black_img_1 = black_img.copy()

sample_img = cv2.cvtColor(black_img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

canny_edged_img = cv2.Canny(sample_img, threshold1=50, threshold2=255)
cv2.imshow("Edged image", canny_edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

ret, contours, hierarchy = cv2.findContours(sample_img, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

for (index, contour) in enumerate(contours):
    centre_of_masses_img = label_contour_center(black_img, contour, index+1)

cv2.imshow("Image with contour centres labeled", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sorting the contours from left to right using x_cord_of_contour function
sorted_contours = sorted(contours, key=lambda x: x_cord_of_contour(x))

for (index, contour) in enumerate(sorted_contours):
    cv2.drawContours(black_img_1, [contour], -1, color=(0, 255, 0), thickness=3)
    cx = x_cord_of_contour(contour)
    cy = y_cord_of_contour(contour)
    cv2.putText(black_img_1, str(index+1), (cx, cy), cv2.FONT_HERSHEY_DUPLEX, 1, (255, 0, 0), 2)

cv2.imshow("Image with contour centres labeled in a SORTED manner from LEFT TO RIGHT", black_img_1)
cv2.waitKey(0)
cv2.destroyAllWindows()