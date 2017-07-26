import cv2, glob

for file in glob.glob("*.jpg"):
    image=cv2.imread(file, 1)
    resized=cv2.resize(image, (100,100))
    cv2.imwrite(file[0:-4] + "_resize.jpg", resized)

# image=cv2.imread("galaxy.jpg",1)
#
# resized_image=cv2.resize(image,(round(image.shape[1]/2),round(image.shape[0]/2)))
# cv2.imshow("galaxy", resized_image)
# cv2.imwrite("resized_galazy_color.jpg", resized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
