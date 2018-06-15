import cv2
import numpy as np

def sketch(img):
    # Conversion to greyscaled image
    grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Using Gaussian blur to smoothen the image, thereby leading to more accurate and less noisy edge detection
    blurred_img = cv2.GaussianBlur(grey_img, (7, 7), 0)

    # Detecting the edges
    edged_img = cv2.Canny(blurred_img, 40, 125)  # An image with white colored edges and black background

    # Now, we are going to give a sketch like effect by the following methods:
    # 1). We will invert edged_img so as to produce an image with black colored edges and white background
    # 2). Then, we will convert the black colored edges into grey colored edges to give more of a like pencil sketch kind of feeling
    # 3). Now, the edges are going to be very thin. So, we will be using morphological operation of Erosion to expand the grey edges
    # (You might think that for expanding edges, dilation should be used but here, the background is white and the edges (objects) are dark, so erosion operation is going to produce dilation operation like output)

    # Step 1).
    inv_edged_img = cv2.bitwise_not(edged_img)

    # Step 2).
    factor = 125  # Higher the value of factor, more the edges are going to be lighter in color. So, a mediocre value like 125 will give a good shade of grey for the edges
    grey_arr = np.ones(grey_img.shape, dtype=np.uint8) * factor
    grey_edged_img = cv2.add(inv_edged_img, grey_arr)

    # Step 3).
    final_sketch = cv2.erode(grey_edged_img, (5, 5))

    return final_sketch


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Output", sketch(frame))

    ## Press 'Esc' button to close the capturing window
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
