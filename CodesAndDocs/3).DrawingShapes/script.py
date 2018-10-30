import cv2
import numpy as np

# Creating a B/W black colored image of 400x400 resolution
black_img = np.zeros((400, 400), np.uint8)

cv2.imshow("Black Image", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

### Firstly, we will divide the black_img into four quadrants

# Creating a vertical line dividing the image into half, vertically
start_vert_x_coordinate, start_vert_y_coordinate = [200, 0]
end_vert_x_coordinate, end_vert_y_coordinate = [200, 400]

# Imposing the vertical line
cv2.line(black_img, (start_vert_x_coordinate, start_vert_y_coordinate), (end_vert_x_coordinate, end_vert_y_coordinate), color=(255, 255, 255), thickness = 2)

# Creating a horizontal line dividing the into half, horizontally
start_hor_x_coordinate, start_hor_y_coordinate = [0, 200]
end_hor_x_coordinate, end_hor_y_coordinate = [400, 200]

# Imposing the horizontal line
cv2.line(black_img, (start_hor_x_coordinate, start_hor_y_coordinate), (end_hor_x_coordinate, end_hor_y_coordinate), color = (255, 255, 255), thickness = 2)

cv2.imshow("Image with quadrants", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

### Now, let's create white colored circles in each quadrant with the radius of 100 pixels thereby, making sure each circle covers the full quadrant
### Then, we will impose black BORDERED circles with half the radius on the existing white circles

radius = 100

# For first quadrant
centre_first_quad_x, centre_first_quad_y = [100, 100]
cv2.circle(black_img, (centre_first_quad_x, centre_first_quad_y), radius, color = (255, 255, 255), thickness = -1)
cv2.circle(black_img, (centre_first_quad_x, centre_first_quad_y), radius//2, color = (0, 0, 0), thickness = 2)

# For second quadrant
centre_second_quad_x, centre_second_quad_y = [100+200, 100]
cv2.circle(black_img, (centre_second_quad_x, centre_second_quad_y), radius, color = (255, 255, 255), thickness = -1)
cv2.circle(black_img, (centre_second_quad_x, centre_second_quad_y), radius//2, color = (0, 0, 0), thickness = 2)

# For third quadrant
centre_third_quad_x, centre_third_quad_y = [100, 100+200]
cv2.circle(black_img, (centre_third_quad_x, centre_third_quad_y), radius, color = (255, 255, 255), thickness = -1)
cv2.circle(black_img, (centre_third_quad_x, centre_third_quad_y), radius//2, color = (0, 0, 0), thickness = 2)

# For fourth quadrant
centre_fourth_quad_x, centre_fourth_quad_y = [100+200, 100+200]
cv2.circle(black_img, (centre_fourth_quad_x, centre_fourth_quad_y), radius, color = (255, 255, 255), thickness = -1)
cv2.circle(black_img, (centre_fourth_quad_x, centre_fourth_quad_y), radius//2, color = (0, 0, 0), thickness = 2)

cv2.imshow("Image with circles and lines", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#### Here, thickness = -1 means that the circle will be filled up with white color instead of being just bordered with white color

# Drawing the final black rectangle.
cv2.rectangle(black_img, (centre_first_quad_x, centre_first_quad_y), (centre_fourth_quad_x, centre_fourth_quad_y), color = (0, 0, 0), thickness = 2)

cv2.imshow("Final Image", black_img)
cv2.waitKey(0)
cv2.destroyAllWindows()