# Imports
import os
import re
import numpy as np
import pandas as pd

def load_data(
        filename: 'str',
        usecols: tuple = None,
        delimiter: str = ',',
        skiprows: int = 0,
        is_pandas: bool = False
        ):
    '''
    Load specific columns from a delimited text file into a NumPy array or a Pandas dataframe.

    Parameters:
        `filename` (str): 
            Name of the file to load, relative to the project root directory.
        `usecols` (tuple of int, optional):
            Tuple (start, end) representing the column range to load (start inclusive, end exclusive).
        `delimiter` (str, optional): 
            Delimiter used in the file. Default is ','.
        `skiprows` (int, optional): 
            Number of initial rows to skip (e.g., header lines). Must be non-negative. Default is 0.

    Returns:
        if `is_pandas` == False:
            numpy.ndarray: 
                A NumPy array containing the loaded data.
        else:
            pandas.DataFrame:
                A Pandas DataFrame containing the loaded data.

    Raises:
        ValueError: 
            If any input parameter is missing or of incorrect type.

    Example:
        data = load_data(filename='data.csv', usecols=(1, 3), skiprows=1)
    '''
    if filename is None:
        raise ValueError('Filename must be provided')
    if not isinstance(filename, str):
        raise ValueError('filename must be a string')
    if usecols is not None and not isinstance(usecols, tuple):
        raise ValueError('usecols must be a tuple')
        if len(usecols) != 2:
            raise ValueError('usecols must be a tuple of length 2')
    if not isinstance(delimiter, str):
        raise ValueError('delimiter must be a string')
    if not isinstance(skiprows, int):
        raise ValueError('skiprows must be an integer')
    if skiprows < 0:
        raise ValueError('skiprows must be a non-negative integer')
    
    # Format paths to access from anywhere
    # Gets to the root through iteratively moving back from folders containing numerical folders
    cwd = os.getcwd()
    while bool(re.search(r'\d-', cwd)):
        cwd = os.path.dirname(cwd)
    root = cwd

    file_path = os.path.join(f'{root}/data', filename)
    if is_pandas:
        if usecols is None:
            data = pd.read_csv(file_path, delimiter=delimiter, skiprows=skiprows)
        else:
            data = pd.read_csv(file_path, delimiter=delimiter, skiprows=skiprows, usecols=np.arange(usecols[0], usecols[1]))
    else:
        if usecols is None:
            data = np.loadtxt(file_path, delimiter=delimiter, skiprows=skiprows)
        else:
            data = np.loadtxt(file_path, delimiter=delimiter, skiprows=skiprows, usecols=np.arange(usecols[0], usecols[1]))
    print('\n=> Data successfully loaded from:\n', file_path)
    print('\n=> data[0:3]:\n', data[0:3])
    print('\n=> Information about the data:')
    print('Ndim =', data.ndim)
    print('Shape =', data.shape)
    print('Size =', data.size)

    return data