import sys
import cv2
import numpy as np
import os

# You should replace these 3 lines with the output in calibration step
DIM=(640, 480)
K=np.array([[256.5223090219522, 0.0, 300.8492878302576], [0.0, 255.95393505302218, 200.83738221162403], [0.0, 0.0, 1.0]])
D=np.array([[-0.03309970266931218], [-0.035713407140983686], [0.03466182058100104], [-0.014366025635664394]])
def undistort(img_path):
    img = cv2.imread(img_path)
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    cv2.imshow("undistorted", undistorted_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
if __name__ == '__main__':
    undistort('Vert0.jpg')
    #for p in sys.argv[1:]:
     #   undistort(p)