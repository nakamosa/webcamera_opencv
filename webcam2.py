import cv2
import numpy as np

def capture_camera(mirror=True, size=None):
    """Capture video from camera"""
    # カメラをキャプチャする
    cap = cv2.VideoCapture(0) # 0はカメラのデバイス番号

    while True:
        # retは画像を取得成功フラグ
        end_flag, frame = cap.read()

        # 鏡のように映るか否か
        if mirror is True:
            frame = frame[:,::-1]

        #tsuchida add start 20180207
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        h = hsv[:, :, 0]
        s = hsv[:, :, 1]
        mask = np.zeros(h.shape, dtype=np.uint8)
#        mask[((h < 20) | (h > 200)) & (s > 128)] = 255
        mask[((h < 20) | (h > 230)) & (s > 228)] = 255
        #num = len(np.where(mask==255))
        num = np.where(mask==255)
        if len(num[0]) > 0:
         cv2.rectangle(img_gray,(258,224),(475,441),(0, 0, 225),3)
         print ('赤')
        else:
         print ('not赤')
        #print('len:{}'.format(np.where(mask==255)))
        #if num > 0:
        #print('num:{}'.format(num))
        #tsuchida add end 20180207
        
       

        # フレームをリサイズ
        # sizeは例えば(800, 600)
        if size is not None and len(size) == 1:
            frame = cv2.resize(frame, size)

        # フレームを表示する
        cv2.imshow('camera capture', img_gray)

        k = cv2.waitKey(1) # 1msec待つ
        if k == 27: # ESCキーで終了
            break

    # キャプチャを解放する
    cap.release()
    cv2.destroyWindows()

capture_camera()
