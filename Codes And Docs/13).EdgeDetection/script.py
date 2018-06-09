import cv2

sample_img = cv2.imread("../sample.png")
cv2.imshow("Original Image", sample_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Edges are points where color intensity or pixel value changes quite vastly
## There are three types of Edge Detection
## Sobel Edge Detection :- To display horizontal or vertical edges
## Laplacian Edge Detection :- Gets all orientations of edges
## Canny Edge Detection :- Optimal and accurate edge detection

##  Canny Edge Detection works in the following way :-
## 1). Apply Gaussian Blur
## 2). Find intensity gradientof the image
## 3). Apply non-maximum suppresion (i.e. removes pixels that are not edges)
## 4). Apply Threshold (Hysteresis) i.e. if pixel is within upper and lower thresholds, it's considered an edge

## For edge detection, it is useless to use a colored image because we just need to determine the edges in the end which will be white colored and background will be black.
## So, the same thing can be done by greyscaled image too.
## So, it's the best option to use greyscaled input image so as to increase the efficiency on image processing
#  because of the presence of one component of pixel value instead of three RGB components of each pixel value in colored images.

greyscale_img = cv2.cvtColor(sample_img, cv2.COLOR_BGR2GRAY)

## Let's do Sobel Edge Detection
sobel_edge_img_x = cv2.Sobel(greyscale_img, cv2.CV_64F, dx=0, dy=1, ksize=5) #Horizontal Edges
sobel_edge_img_y = cv2.Sobel(greyscale_img, cv2.CV_64F, dx=1, dy=0, ksize=5) #Vertical Edges
sobel_edge_img = cv2.bitwise_or(sobel_edge_img_x, sobel_edge_img_y) # Imposing them on each other via OR operation to produce the final sobel edge detected image

## Now, Let's do Laplacian Edge Detection
laplacian_edge_img = cv2.Laplacian(greyscale_img, cv2.CV_64F)

## Now, Let's do Canny Edge Detection
canny_edge_img = cv2.Canny(greyscale_img, threshold1=55, threshold2=175)

## Displaying the outputs
cv2.imshow("Sobel Edge Detected Image", sobel_edge_img_x)
cv2.waitKey(0)

cv2.imshow("Laplacian Edge Detected Image", sobel_edge_img_y)
cv2.waitKey(0)

cv2.imshow("Canny Edge Detected Image", sobel_edge_img)
cv2.waitKey(0)
cv2.destroyAllWindows()