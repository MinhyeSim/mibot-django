#모델들을 각각 만들어 api로 연결하는 형태를 목표로 둔다.
# 객체지향으로 코딩하지 말기
import matplotlib.pyplot as plt
from keras.datasets import mnist
from tensorflow import keras
import tensorflow as tf

_, (x_test, y_test) = mnist.load_data()
x_test = x_test / 255.0 # 데이터 정규화
model = tf.keras.models.load_model('./save/mnist_model.h5')

#model.summary()
model.evaluate(x_test, y_test, verbose=2)
plt.imshow(x_test[30], cmap="gray")
plt.show()
picks = [30]
#predict = model.predict_classes(x_test[picks])
y_prob = model.predict(x_test[picks], verbose=0)
predicted = y_prob.argmax(axis=-1)

print("손글씨 예측값: ", predicted)