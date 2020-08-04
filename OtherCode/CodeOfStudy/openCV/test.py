import cv2 as cv
src=cv.imread('d:\\15825158_cover.jpg')
cv.namedWindow('input_image',cv.WINDOW_AUTOSIZE)
print(src.shape)
src2=src-50
print(src2)
# print(src2)
cv.imshow('input_image',src2)
# cv.imshow('input_image',src)
cv.waitKey(0)
cv.destroyAllWindows()

