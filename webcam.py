import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    
    # フレームを取得
    frame = cv2.imread("DEF.jpg",cv2.COLOR_BGR2HSV)
    
    # フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # 取得する色の範囲を指定する
    lower_yellow = np.array([0, 150, 0])
    upper_yellow = np.array([255, 255, 255])
    
    # 指定した色に基づいたマスク画像の生成
    img_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    
    # フレーム画像とマスク画像の共通の領域を抽出する。
    img_color = cv2.bitwise_and(frame, frame, mask=img_mask)
    
    cv2.imshow("SHOW COLOR IMAGE", img_color)
    
    # qを押したら終了
    k = cv2.waitKey(1)
    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
