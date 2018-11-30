import SudoFunctions
import cv2
import numpy


sudo_img = cv2.imread('/Users/luizfper/PycharmProjects/Sudoku/images/Sudo1.jpeg',cv2.IMREAD_GRAYSCALE)

sudo_img_proc = cv2.GaussianBlur(sudo_img,(9,9),0)
sudo_img_proc = cv2.adaptiveThreshold(sudo_img_proc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
sudo_img_proc = cv2.adaptiveThreshold(sudo_img_proc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
#sudo_img_proc = cv2.dilate(sudo_img_proc,kernel)

sudo_img_proc = cv2.bitwise_not(sudo_img_proc)


new_img, ex_contours, hier = cv2.findContours(sudo_img_proc,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
new_img, contours, hier = cv2.findContours(sudo_img_proc,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

sudo_img_proc=cv2.cvtColor(sudo_img_proc,cv2.COLOR_GRAY2BGR)

kernel = numpy.ones((3, 3), numpy.uint8)
sudo_img_proc = cv2.dilate(sudo_img_proc, kernel)

all_contours = cv2.drawContours(sudo_img_proc.copy(), contours, -1, (255, 0, 0), 1)
external_only = cv2.drawContours(sudo_img_proc.copy(), ex_contours, -1, (255, 0, 0), 1)

contours = sorted(contours,key=cv2.contourArea,reverse=True)
polygon = contours[0]

#bottom_right = max()#

cv2.imshow('image', external_only)
cv2.waitKey(0)
cv2.destroyAllWindows()

