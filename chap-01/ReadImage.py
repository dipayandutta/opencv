import cv2

print("package Imported!")

# load the image
img = cv2.imread("Resources\images\lena.png")

#Display the image
cv2.imshow("Output",img)

#add Delay
cv2.waitKey(0) #0== infinte delay
