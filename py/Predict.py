import operator
from alpabet_trans import alpha

class Predic():
    result = []
    def Predict(self,model,real):
        my_list = model.predict(real)
        index, value = max(enumerate(my_list[0]), key=operator.itemgetter(1))       # 확률이 가장 높은 것 반환
        print(index,alpha(index))
        self.result.append(alpha(index))

        return self.result

    def reset(self):
        self.result = []

def chk_trans():
    for i in range(0, 27):
        print(str(i) + ':' + alpha(i),end='  ')
        if i%3 ==2 :
            print()
