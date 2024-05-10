import numpy as np
from ops import FF


min_input_layer = np.array(
    [
        [1, -1, 1],
        [0, 0, -1]
    ]
)
min_output_layer = np.array([1, -1, -1])
max_input_layer = np.array(
    [
        [1, -1, -1],
        [0, 0, 1]
    ]
)
max_output_layer = np.array([1, -1, 1])
sum_input_layer = np.array(
   [
       [1, 0],
       [-1, 0],
       [0, 1],
       [0, -1],
   ]
).T
sum_output_layer = np.array([1, -1, 1, -1])
min_ff = FF(min_input_layer, min_output_layer)
max_ff = FF(max_input_layer, max_output_layer)
sum_ff = FF(sum_input_layer, sum_output_layer)
print(min_ff([89, 98]))
print(max_ff([59, 98]))
print(min_ff)
print(max_ff)
print(sum_ff([89, 98]))
print(sum_ff)
print(sum_ff([-59, 98]))
print(sum_ff)
