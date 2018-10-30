import cv2

### Here, we are going to approximate contours from a set of given contours
### The function we are going to use is going to cv2.approxPolyDP(contour, approximation accuracy, closed)
### -- contour - its the individual contour we wish to approximate
### -- approximation accuracy - Important parameter for determining the accuracy of the approximation. Small
###     values give precise and large values give more generic approximations.
###     A good rule of thumb is less than 5% of the contour perimeter
### -- closed - a boolean value that states whether the approximate contour should be open or closed

## Reading the image of the outline of a house
image = cv2.imread("./house.jpg")
orig_image = image.copy()

## Displaying the original image
cv2.imshow("Original Image", orig_image)
cv2.waitKey(0)

## Converting the image to greyscale
gray = cv2.cvtColor(orig_image, cv2.COLOR_BGR2GRAY)

## Binarizing the image
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)

## Displaying the contours in the original image

### Finding contours
_, contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
### Displaying the contours
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(orig_image, (x, y), (x+w, y+h), (0, 0, 255), 2)
    cv2.imshow("Bounding rectangles", orig_image)
cv2.waitKey(0)


## Displaying the approximated contours
for c in contours:

    ## keeping the approximation accuracy = 3% of the perimeter of the contour
    accuracy = 0.03*cv2.arcLength(c, closed=True)
    approx = cv2.approxPolyDP(c, accuracy, True)
    cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
    cv2.imshow("Approx Poly DP", image)

cv2.waitKey(0)
cv2.destroyAllWindows()