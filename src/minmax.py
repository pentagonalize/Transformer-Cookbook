import numpy as np
from ops import ReLU, Linear, Sequential


min_input_layer = np.array(
    [
        [1, -1, 1],
        [0, 0, -1]
    ]
)
max_input_layer = np.array(
    [
        [1, -1, -1],
        [0, 0, 1]
    ]
)
min_output_layer = np.array([1, -1, -1])
max_output_layer = np.array([1, -1, 1])
min_ff = Sequential(
    [
        Linear(min_input_layer),
        ReLU(),
        Linear(min_output_layer)
    ]
)
max_ff = Sequential(
    [
        Linear(max_input_layer),
        ReLU(),
        Linear(max_output_layer)
    ]
)
print(min_ff([89, 98]))
print(max_ff([59, 98]))
print(min_ff)
print(max_ff)
