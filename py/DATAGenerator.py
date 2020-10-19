import os
from keras.preprocessing.image import ImageDataGenerator

def data_ready():
    images_dir = './images'

    datagen = ImageDataGenerator(rotation_range=10,
                                 shear_range=10,
                                 validation_split=0.2,
                                 ) #20%를 검증모델로 사용.

    train_generator = datagen.flow_from_directory(images_dir,
                                                  target_size=(28,28),
                                                  subset='training')

    val_generator = datagen.flow_from_directory(images_dir,
                                                target_size=(28,28),
                                                subset='validation')

    return train_generator, val_generator

def load_image(img_path):
    images_dir = img_path
    datagen = ImageDataGenerator()
    real_generator = datagen.flow_from_directory(images_dir,
                                                 target_size=(28, 28))

    return real_generator



