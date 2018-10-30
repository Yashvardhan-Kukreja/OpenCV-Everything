import cv2
import numpy as np

### Convex Hull is something that looks at the outer edges of the image and it can be used to draw lines to each of the outer edges there
### Basically, Convex hull can be used to produce the smallest polygon which can fit around the given object

image = cv2.imread("./hand.jpg")
orig_image = image.copy()
cv2.imshow("Original Image", orig_image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
cv2.imshow("Thresholded Image", thresh)
cv2.waitKey(0)

_, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

## Let's find the convex hull
for c in contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(orig_image, [hull], 0, (0, 0, 255), 2)
    cv2.imshow("Convex Hull", orig_image)

cv2.waitKey(0)

### Now, here is a problem.
### Due to the background of thresholded image being white
### One of the contours will be a box covering the whole background
### But we don't need it all because we want the contour of the hand only

### So, what we're going to do is that we 're going to sort the contours by area
## And remove the contour with the biggest area which basically is gonna be the box covering the whole background

sorted_contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse=True)[1:]

## Finding the convex hull only for the hand
for c in sorted_contours:
    hull = cv2.convexHull(c)
    cv2.drawContours(image, [hull], 0, (0, 255, 0), 2)
    cv2.imshow("Convex Hull (fixed)", image)

cv2.waitKey(0)
cv2.destroyAllWindows()