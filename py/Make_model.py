
from keras import backend as K
from keras import layers as L
from keras.models import Model
from keras.regularizers import l2
from keras.callbacks import ModelCheckpoint,ReduceLROnPlateau,EarlyStopping

def Make_model(train,val):
    K.clear_session()

    model_ckpt = ModelCheckpoint('BrailleNet.h5',save_best_only=True)       # 결과저장
    reduce_lr = ReduceLROnPlateau(patience=8,verbose=0)
    early_stop = EarlyStopping(patience=20,verbose=2)                       # 변화가 없으면 중지


    # SeparableConv2D > 좋은 모델 사용
    entry = L.Input(shape=(28,28,3))
    x = L.SeparableConv2D(64,(3,3),activation='relu')(entry)
    x = L.MaxPooling2D((2,2))(x)
    x = L.SeparableConv2D(128,(3,3),activation='relu')(x)
    x = L.MaxPooling2D((2,2))(x)
    x = L.SeparableConv2D(256,(2,2),activation='sigmoid')(x)
    x = L.GlobalMaxPooling2D()(x)
    x = L.Dense(256)(x)
    x = L.LeakyReLU()(x)
    x = L.Dense(64,kernel_regularizer=l2(2e-4))(x)
    x = L.LeakyReLU()(x)
    x = L.Dense(27,activation='softmax')(x)

    model = Model(entry,x)
    model.compile(loss='categorical_crossentropy',optimizer='adam',metrics=['accuracy'])

    history = model.fit_generator(train,validation_data=val,epochs=666,
                                  callbacks=[model_ckpt,reduce_lr,early_stop],verbose=0)
    return history

def print_acc_loss(history):
    # 평가 결과 도식화
    import matplotlib.pyplot as plt
    fig, loss_ax = plt.subplots(figsize=(10, 5))
    acc_ax = loss_ax.twinx()
    loss_ax.plot(history.history['loss'], 'y', label='train loss')
    loss_ax.plot(history.history['val_loss'], 'r', label='val loss')
    acc_ax.plot(history.history['accuracy'], 'b', label='train acc')
    acc_ax.plot(history.history['val_accuracy'], 'g', label='val acc')
    loss_ax.set_xlabel('epoch')
    loss_ax.set_ylabel('loss')
    acc_ax.set_ylabel('accuray')
    loss_ax.legend(loc='upper left')
    acc_ax.legend(loc='lower left')

    plt.show()