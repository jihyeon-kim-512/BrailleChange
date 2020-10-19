#
import matplotlib.pyplot as plt
from matplotlib import font_manager,rc


font_path = 'D:/ML/08_13/malgun.ttf'

#폰트 이름 얻어오기
font_name = font_manager.FontProperties(fname=font_path).get_name()
#font 설정
rc('font',family=font_name)


def plot_loss(history):
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('모델 손실')
    plt.ylabel('손실')
    plt.xlabel('반복')
    plt.legend(['학습', '검증'], loc=0)


def plot_acc(history):
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('모델 정확도')
    plt.ylabel('정확도')
    plt.xlabel('반복')
    plt.legend(['학습', '검증'], loc=0)

