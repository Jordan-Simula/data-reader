import numpy as np
from scipy.io import arff


def read_arff(file_name):
    # Load ARFF file
    data, meta = arff.loadarff(file_name)

    # Convert to numpy array
    return np.array(data.tolist())

numpy_array = read_arff('auto_mpg.arff')
print(numpy_array[0])
print(numpy_array[-1])
print(numpy_array.shape)