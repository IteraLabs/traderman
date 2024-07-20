from typing import NewType
from attr import validators
from attrs import define
import torch
import numpy as np

torchTensor = NewType("torchTensor", torch.Tensor)
numpyArray = NewType("numpyArray", np.ndarray)


@define(slots=True, frozen=True)
class tensorTypes:
    torchTensor = torchTensor
    numpyArray = numpyArray
    validator = [
        validators.instance_of(torch.Tensor),
        validators.instance_of(np.ndarray),
    ]
