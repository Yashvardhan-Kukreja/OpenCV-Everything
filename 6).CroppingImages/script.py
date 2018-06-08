import cv2

sample_img = cv2.imread("../sample.png")

height, width = sample_img.shape[:2]

start_row, start_col = int(height*0.4), int(width*0.4)
end_row, end_col = int(height*0.8), int(height*0.8)

cropped_img = sample_img[start_row:end_row, start_col:end_col]

cv2.imshow("Cropped Image", cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()