import DATAGenerator
from PIL import Image
import os

class img_devide():
    def __init__(self,img_path):
        self.img_path = img_path
        self.path = ''
        self.call_num = 0
        self.lengh = 0
        self.width = 0
        self.height = 0
        self.img = ''


    def create_dir(self):
        try:
            os.mkdir('./test/a')
            print('create new dir')
        except:
            print('already exist')
            pass
        self.path = './test/a'

    def devide_img(self):
        self.img = Image.open(self.img_path)
        area = (0+self.call_num*self.height,0,self.width/self.lengh*(self.call_num+1),self.height)      # 자르는 범위 설정

        cropped_img = self.img.crop(area)       # 이미지를 자름
        cropped_img.save(self.path + '/'+str(self.call_num)+'.jpg')     # 이미지 저장

        self.call_num+=1        # 불러진 순서


    def set_image(self):
        self.img = Image.open(self.img_path)
        self.width = self.img.size[0]
        self.height = self.img.size[1]
        self.lengh = int(self.width / self.height)


    # 임시 파일 제거
    def remove_file(self):
        try:
            os.remove(self.path+'/'+str(self.call_num-1)+'.jpg')
        except:
            pass


    # 임시파일 경로 제거 (근데 안씀)
    def remove_dir(self) :
        try:
            os.rmdir(self.path)
        except :
            print('fail')

