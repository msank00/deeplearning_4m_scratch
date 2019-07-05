
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: dev_nb/02_fully_connected.ipynb

from exp.nb_01 import *

def get_data():
    path = datasets.download_data(MNIST_URL, ext='.gz')
    with gzip.open(path, 'rb') as fin:
        ((x_train, y_train), (x_valid, y_valid), _) = pickle.load(fin, encoding='latin-1')

    return map(tensor, (x_train, y_train, x_valid, y_valid))

def normalize(x:torch.Tensor,
              mean: torch.Tensor,
              std: torch.Tensor) -> torch.Tensor:

    return (x - mean)/std

def test_near_zero(value, tol:float=1e-3):
    assert value.abs()<tol, f"Near Zero: {value}"

from torch.nn import init

def mse(output, targ): return (output.squeeze(-1) - targ).pow(2).mean()

from torch import nn