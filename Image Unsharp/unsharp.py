import cv2
import numpy as np

image = cv2.imread(r"dog1.jpg")
b, g, r = cv2.split(image)
ori_img = image.copy()
cv2.imshow('orig_dog', image) 


a_p = 10.0
b_p = 1.0
A = np.array([[1, 4, 7, 4, 1],
              [4, 16, 26, 16, 4],
              [7, 26, 41, 26, 7],
              [4, 16, 26, 16, 4],
              [1, 4, 7, 4, 1]])

# A = np.array([
#              [1,2,1],
#              [2,4,2],
#              [1,2,1],
#             ])

sum_A = np.sum(A)
for i in range(1, image.shape[0] - 2): # if A is 3x3, then the index will be "image.shape[0] - 1"
        for j in range(1, image.shape[1] - 2):
                value0 = 0
                value1 = 0
                value2 = 0
                for k in range(5): # depends on filter size
                        for l in range(5):
                                value0 = value0 + b[(i + k) - 2][(j + l) - 2] * A[k][l]
                                value1 = value1 + g[(i + k) - 2][(j + l) - 2] * A[k][l]
                                value2 = value2 + r[(i + k) - 2][(j + l) - 2] * A[k][l]
                b[i][j] = value0 / sum_A
                g[i][j] = value1 / sum_A
                r[i][j] = value2 / sum_A
blur_image = cv2.merge([b, g, r])
cv2.imshow('blur_dog', blur_image)
cv2.imwrite("blur_dog.jpg", blur_image)

result_image = cv2.addWeighted(ori_img, a_p + b_p, blur_image, -a_p, 0, ori_img) 
# (原始影像, 原始圖權重, 模糊後的影像, 模糊影像權重, 兩圖相加再相減的值(這邊沒用到設0), 輸出圖)
# Unsharp 公式
# Inew = a*( Iori – Ilowpass) + b* Iori　　→　　Inew = (a+b)* Iori - a* Ilowpass 

cv2.imshow('result_dog', result_image)
cv2.imwrite("result_dog.jpg", result_image)
cv2.waitKey(0)