import numpy as np

"""
    load the matrix from the text file using numpy
    :param file_path: path to the file
    :return: matrix
"""
def load_matrix(file_path):
    return np.loadtxt(file_path, delimiter=',')