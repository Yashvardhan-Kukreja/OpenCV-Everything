import cv2
import numpy as np

## I will explain perspective transformation via an example
## So, let's say, I have an image containing a table and on that table, a sheet of paper is lying
## Now, what I want as the output is the image only of the sheet without any parts of table involved
## Basically, it is going to be like cropping out specifically the sheet of paper from the image
## The app "CamScanner" does the same
## So, for doing this kind of thing, we apply perspective transformation on the original image

## So, here, first of all, we take four coordinates of the original enclosing the region which want to be cropped out. The variable coords_1
## And then, we take four other coordinates "coords_2". The cropped out image will be enclosed under these coordinates "coords_2"
## This is a bit tricky. So, it will be good to explore official documentation OpenCV python for this topic

sample_img = cv2.imread("../sample.png")

# Displaying the input image
cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

coords_1 = np.array([[300, 100], [600, 200], [300, 600], [600, 400]], dtype=np.float32)

coords_2 = np.array([[0, 0], [600, 0], [0, 400], [600, 400]], dtype=np.float32)

persepective_mat = cv2.getPerspectiveTransform(coords_1, coords_2)

output_img = cv2.warpPerspective(sample_img, persepective_mat, (600, 400))

# Highlighting coordinates and region on the input image
radius = 15
cv2.circle(sample_img, (300, 100), radius, color=(0, 255, 0), thickness=-1)
cv2.circle(sample_img, (600, 200), radius, color=(0, 255, 0), thickness=-1)
cv2.circle(sample_img, (300, 600), radius, color=(0, 255, 0), thickness=-1)
cv2.circle(sample_img, (600, 400), radius, color=(0, 255, 0), thickness=-1)
cv2.line(sample_img, (300, 100), (600, 200), color=(255, 255, 255), thickness=2)
cv2.line(sample_img, (600, 200), (600, 400), color=(255, 255, 255), thickness=2)
cv2.line(sample_img, (600, 400), (300, 600), color=(255, 255, 255), thickness=2)
cv2.line(sample_img, (300, 600), (300, 100), color=(255, 255, 255), thickness=2)


# Displaying the input image with highlighted coordinates
cv2.imshow("Original Image perspective coordinates", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Displaying the output image
cv2.imshow("Output perspective image", output_img)
cv2.waitKey(0)
cv2.destroyAllWindows()