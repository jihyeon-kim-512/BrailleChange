import cv2, os
import numpy as np

class scanner_b():

  def __init__(self,img_path):
    self.img_path = img_path
    self.filename, ext = os.path.splitext(os.path.basename(self.img_path))
    self.ori_img = cv2.imread(self.img_path)
    self.src = []
    #self.len = lens


  # mouse callback handler
  def mouse_handler(self,event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
      img = self.ori_img.copy()

      self.src.append([x, y])

      for xx, yy in self.src:
        cv2.circle(img, center=(xx, yy), radius=5, color=(255,255 , 255), thickness=1, lineType=cv2.LINE_AA)

      cv2.imshow('img', img)

      # perspective transform
      if len(self.src) == 4:
        src_np = np.array(self.src, dtype=np.float32)

        width = max(np.linalg.norm(src_np[0] - src_np[1]), np.linalg.norm(src_np[2] - src_np[3]))
        height = max(np.linalg.norm(src_np[0] - src_np[3]), np.linalg.norm(src_np[1] - src_np[2]))

        dst_np = np.array([
          [0, 0],
          [width, 0],
          [width, height],
          [0, height]
        ], dtype=np.float32)

        M = cv2.getPerspectiveTransform(src=src_np, dst=dst_np)
        result = cv2.warpPerspective(self.ori_img, M=M, dsize=(width, height))
        dst = cv2.resize(result, dsize=(int(width*1.2), height), interpolation=cv2.INTER_AREA)

        cv2.imshow('result', dst)
        cv2.imwrite('./real/a/l.jpg', dst)
        #cv2.imwrite('./result/%s_result%s' % (self.filename, self.ext), result)




  def start(self):

    cv2.namedWindow('img')
    cv2.setMouseCallback('img', self.mouse_handler)

    cv2.imshow('img', self.ori_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    exit()

a = scanner_b('./real/a/pic2.jpg')
a.start()

