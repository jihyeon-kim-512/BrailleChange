import os
from shutil import copyfile

def Preset():

    try:
        os.mkdir('./images/')
        alpha = 'a'

        # 이미지가 들어갈 폴더 준비
        print("=== DIR Ready ===")
        for i in range(0, 26):
            os.mkdir('./images/' + alpha)
            alpha = chr(ord(alpha) + 1)

        os.mkdir('./images/zz')     # 공백 폴더

        print("=== Start Copy Image ===")

        # 이미지 확인 후 알파벳 별로 폴더 분류
        rootdir = './Braille Dataset/Braille Dataset2/'
        for file in os.listdir(rootdir):
            letter = file[0]
            if file[1] == 'z':     # 공백 폴더
                pass
            else:
                copyfile(rootdir+file, './images/' + letter + '/' + file)

        for file in os.listdir(rootdir):
            letter = file[1]
            if letter == 'z':
                copyfile(rootdir + file, './images/zz/' + file)

        print("=== Image Ready Complete ===")
    except:
        print("Images already exist!")
        pass
