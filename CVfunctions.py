import SudoFunctions
import cv2

def test_solving():

    sudao = []
    sudao = [8,0,0,0,0,0,0,0,0,0,0,3,6,0,0,0,0,0,0,7,0,0,9,0,2,0,0,0,5,0,0,0,7,0,0,0,0,0,0,0,4,5,7,0,0,0,0,0,1,0,0,0,3,0,0,0,1,0,0,0,0,6,8,0,0,8,5,0,0,0,1,0,0,9,0,0,0,0,4,0,0]
    SudoFunctions.solve_sudoku(sudao)

sudo_img = cv2.imread('/Users/luizfper/PycharmProjects/Sudoku/images/Sudo1.jpeg',cv2.IMREAD_GRAYSCALE)

sudo_img_proc = cv2.GaussianBlur(sudo_img,(9,9),0)
sudo_img_proc = cv2.adaptiveThreshold(sudo_img_proc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
sudo_img_proc = cv2.adaptiveThreshold(sudo_img_proc,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

cv2.imshow('image', sudo_img_proc)
cv2.waitKey(0)
cv2.destroyAllWindows()
