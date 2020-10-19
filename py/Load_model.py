
def load_model():
    from keras.models import load_model
    model = load_model('BrailleNet.h5')
    return model

def acc_chk(model, val):
    acc = model.evaluate_generator(val)[1]
    print('model accuracy: {}'.format(round(acc,4)))