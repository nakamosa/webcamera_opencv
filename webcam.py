import cv2
import numpy as np

while(1):
    
    # フレームを取得
    frame = cv2.imread("p.jpg",cv2.COLOR_BGR2HSV)
    
    # フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV_FULL)
    
    # 取得する色の範囲を指定する
    lower_yellow = np.array([30, 48, 100])
    upper_yellow = np.array([255, 255, 255])
    
    # 指定した色に基づいたマスク画像の生成
    img_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # フレーム画像とマスク画像の共通の領域を抽出する。
    img_color = cv2.bitwise_and(frame, frame, mask=img_mask)
    
#    imgray = cv2.cvtColor(img_color,cv2.COLOR_BGR2GRAY)
#    ret,thresh = cv2.threshold(imgray,127,255,cv2.THRESH_BINARY)
#    image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#    img = cv2.drawContours(img_color, contours, -1, (0,255,0), 10)


    gray_mask = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    ret, threth = cv2.threshold(gray_mask, 127, 255, cv2.THRESH_BINARY)
    gray_mask, countours, hierarchy = cv2.findContours(threth, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img_color, countours, -1, (0, 255, 0), 1)
    
    
    imgEdge,contours,hierarchy = cv2.findContours(threth, 1, 2)

    cnt = contours[0]
    perimeter = cv2.arcLength(cnt,True)
    
    cv2.imshow("perimeter", img_color)
    i = (50*perimeter)/130  #縦のピクセル数
    j = 50/i  #1ピクセル辺りの長さ(mm)
    k = i*j  #確認用
    print("縦の長さ", k,"mm")
    
    # qを押したら終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break


cv2.destroyAllWindows()
