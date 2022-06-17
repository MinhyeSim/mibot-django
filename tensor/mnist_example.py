import tensorflow as tf

class Solution(object):
    def __init__(self):
        self.mnist = None
        self.x_train = None
        self.x_test = None
        self.model = None


    def hook(self):
        def print_menu():
            print('0. Exit')
            print('1. 데이터 로드')
            print('2. 모델 생성')
            print('3. 모델을 훈련하고 평가')
            print('4. 테스트')
            return input('메뉴 선택 \n')

        while 1:
            menu = print_menu()
            if menu == '0':
                break
            elif menu == '1':
                self.data_load()
            elif menu == '2':
                self.create_model()
            elif menu == '3':
                self.training_evaluation_models()
            elif menu == '3':
                self.test()

    def data_load(self):
        minst = self.mnist
        (x_train, y_train),(x_test, y_test) = minst.load_data()
        self.x_train, self.x_test = x_train / 255.0, x_test / 255.0

    def create_model(self):
        self.model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape=(28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dropout(0.2),
            tf.keras.layers.Dense(10, activation='softmax')
        ])

        self. model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        # accuracy'= 평균 = ratio

        #Sequen객체가 있다. () 생성자 처리 -> 객체라는 것은 이닛이 있을 것이다

    def training_evaluation_models(self):
        self.model.fit(self.x_train, self.y_train, epochs=5)
        self.model.evaluate(self.x_test, self.y_test, verbose=2)
        #vervose : 결과에 대해서 코멘트

    def test(self):
        pass


if __name__ == '__main__':
    Solution().hook()