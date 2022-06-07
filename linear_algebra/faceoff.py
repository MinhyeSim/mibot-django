from matplotlib import pyplot as plt
from sklearn.datasets import fetch_olivetti_faces
from matplotlib import rc, font_manager
rc('font', family=font_manager.FontProperties(fname='C:/Windows/Fonts/malgunsl.ttf').get_name())

class Face_off:
    def __init__(self):
        self.faces = fetch_olivetti_faces()
        self.f, ax = plt.subplots(1, 3)

    def solution(self):
        faces = fetch_olivetti_faces()
        f, ax = plt.subplots(1, 3)

        ax[0].imshow(faces.images[6], cmap=plt.cm.bone)
        ax[0].grid(False)
        ax[0].set_xticks([])
        ax[0].set_yticks([])
        ax[0].set_title("image 1: $x_1$")

        ax[1].imshow(faces.images[10], cmap=plt.cm.bone)
        ax[1].grid(False)
        ax[1].set_xticks([])
        ax[1].set_yticks([])
        ax[1].set_title("image 2: $x_2$")

        new_face = 0.7 * faces.images[6] + 0.3 * faces.images[10]
        ax[2].imshow(new_face, cmap=plt.cm.bone)
        ax[2].grid(False)
        ax[2].set_xticks([])
        ax[2].set_yticks([])
        ax[2].set_title("image 3: $0.7x_1 + 0.3x_2$")

        plt.show()

if __name__ == '__main__':
    Face_off().solution()