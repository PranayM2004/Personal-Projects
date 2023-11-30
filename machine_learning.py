import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

class MachineLearning:
    def __init__(self):
        self.model = Sequential([
            Dense(units=64, activation='relu', input_dim=1),
            Dense(units=1, activation='linear')
        ])
        self.model.compile(optimizer='adam', loss='mean_squared_error')

    def train_model(self, training_data):
        # Assume training_data is a list of tuples (input, output)
        x_train = np.array([input_data for input_data, _ in training_data])
        y_train = np.array([output_data for _, output_data in training_data])

        self.model.fit(x_train, y_train, epochs=10)

    def generate_response(self, input_data):
        # Assume input_data is a single input
        input_array = np.array([input_data])
        response = self.model.predict(input_array)

        return response[0]
