import cv2

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image=cv2.imread("news.jpg")

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

faces=face_cascade.detectMultiScale(gray_image,
scaleFactor=1.05,
minNeighbors=5)

for x,y,w,h in faces:
    image=cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 3)

resized = cv2.resize(image, (int(image.shape[1]/2),int(image.shape[0]/2)))
cv2.imshow("image", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
