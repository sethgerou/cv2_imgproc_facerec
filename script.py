import cv2

image=cv2.imread("galaxy.jpg",1)

resized_image=cv2.resize(image,(round(image.shape[1]/2),round(image.shape[0]/2)))
cv2.imshow("galaxy", resized_image)
cv2.imwrite("resized_galazy_color.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
