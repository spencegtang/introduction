
import os
import torch
import torch.nn as nn


if __name__ == '__main__':
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    print(device)
