import keras
import numpy as np


class mnist_model:
    def __init__(self) -> None:
        self.model = keras.models.load_model('mnist.h5')
        self.prediction = None

    def predict(self, arr: np.ndarray) -> None:
        self.prediction = self.model.predict(arr)

    def reset(self) -> None:
        self.prediction = None
