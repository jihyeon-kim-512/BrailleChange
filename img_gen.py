from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

datagen = ImageDataGenerator(   # 이미지 조정해서 불러오기
        rotation_range=10,      # 시계방향으로 회전
        width_shift_range=0.1,  # 가로로 이동
        height_shift_range=0.1, # 세로로 이동
        shear_range=0.1,        # 반시계방향으로 이동
        zoom_range=0.01,        # 확대축소
        fill_mode='nearest'     # 빈공간 처리
        )


# 이미지 가져와서 변경 후 저장
'''
alpha = 'a'

for j in range (0,26):

    img = load_img('./Braille Dataset/ex/'+alpha+'.jpg')  # PIL 이미지
    x = img_to_array(img)  # (3, 150, 150) 크기의 NumPy 배열
    x = x.reshape((1,) + x.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열

    # 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
    # 지정된 `preview/` 폴더에 저장합니다.
    i = 0
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir='./Braille Dataset/Braille Dataset2', save_prefix=alpha, save_format='jpg'):
        i += 1
        if i > 20:
            break  # 이미지 20장을 생성하고 마칩니다

    alpha = chr(ord(alpha) + 1)
'''

# 학습이 덜 된 알파벳 강화학습
alpha = 'y'
img = load_img('./Braille Dataset/ex/'+alpha+'.jpg')  # PIL 이미지
x = img_to_array(img)  # (3, 150, 150) 크기의 NumPy 배열
x = x.reshape((1,) + x.shape)  # (1, 3, 150, 150) 크기의 NumPy 배열

# 아래 .flow() 함수는 임의 변환된 이미지를 배치 단위로 생성해서
# 지정된 `preview/` 폴더에 저장합니다.
i = 0
for batch in datagen.flow(x, batch_size=1,
                      save_to_dir='./Braille Dataset/Braille Dataset2', save_prefix=alpha, save_format='jpg'):
    i += 1
    if i > 100:
     break  # 이미지 20장을 생성하고 마칩니다
