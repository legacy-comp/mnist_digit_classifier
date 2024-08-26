import keras
import numpy as np


class mnist_model:
    def __init__(self) -> None:
        """Model Object used to simplify `mnist model` integration.
        """

        self.model = keras.models.load_model('mnist.h5')
        self.prediction = None


    def predict(self, arr: np.ndarray) -> None:
        """Saves the `model` prediction in `prediction`.

        Parameters
        ----------
        arr : np.ndarray
            accepts numpy array (required shape: 1x784)
        """

        self.prediction = self.model.predict(arr)


    def reset(self) -> None:
        """Clears the `prediction`.
        """
        
        self.prediction = None
