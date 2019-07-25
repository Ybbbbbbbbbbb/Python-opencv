import numpy as np
import cv2
import math



def bilinear(origi_img, max_w=1000, max_h=1200):
    H, W, C = origi_img.shape

    scale = min(max_h/H, max_w/W)

    resize_img = np.zeros((int(H*scale), int(W*scale), C), dtype=np.uint8)

    for c in range(3): # 通道数
        for w in range(int(W*scale)):
            for h in range(int(H*scale)):
                # 求出resize_img在原图上的对应点    
                origin_x = (w+0.5) / scale - 0.5
                origin_y = (h+0.5) / scale - 0.5


                tl_x = math.floor(w/scale) # 左上x
                tl_y = math.floor(h/scale) # 左上y
                br_x = min(tl_x+1, W-1)    # 右下x
                br_y = min(tl_y+1, H-1)    # 右下y

                # 插值
                value_m = (br_x - origin_x) * origi_img[tl_y, tl_x, c] + (origin_x - tl_x) * origi_img[tl_y, br_x, c]
                value_n = (br_x - origin_x) * origi_img[br_y, tl_x, c] + (origin_x - tl_x) * origi_img[br_y, br_x, c]
                resize_img[h,w,c] = int(value_m * (br_y - origin_y) + value_n * (origin_y - tl_y) )

    return resize_img




if __name__ == "__main__":
    origin_img = cv2.imread('girl.jpg')
    resize_img = bilinear(origin_img)
    # img_out = resize(origin_img, (600,600))
    cv2.imshow('girl', resize_img)
    cv2.imshow('原图', origin_img)
    cv2.waitKey(0)