from dataclasses import dataclass
from typing import List, Callable


def ReLU():
    return lambda x: x * (x > 0)


def Linear(W):
    return lambda x: x @ W


@dataclass
class Sequential:
    layers: List[Callable]

    def __init__(self, layers):
        self.layers = layers
        self.activations = [None for _ in range(len(self.layers) + 1)]

    def __call__(self, x):
        self.activations[0] = x
        for i, layer in enumerate(self.layers, start=1):
            x = layer(x)
            self.activations[i] = x
        return x

    def __str__(self):
        return str(self.activations)
