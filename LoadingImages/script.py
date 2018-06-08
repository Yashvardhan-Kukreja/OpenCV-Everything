import cv2

# Reading the sample image
sample_img = cv2.imread("../sample.png")

# Displaying the sample image in a window with title "Sample Image"
cv2.imshow("Sample Image", sample_img)

# Whenever a keystroke is pressed on the keyboard, the output image window will close
cv2.waitKey(0)
cv2.destroyAllWindows()