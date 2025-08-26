"""
==============================================
Oracle ONE - Data Science Course
==============================================

File: load_data.py
Author: Mateus Alves de Mendonça
Description: Utility functions for loading data from various file formats
Created: Oracle ONE Data Science Program
License: MIT

This module provides flexible data loading functions that support
both NumPy arrays and Pandas DataFrames with type hints.
"""

# Standard library imports
import os
from typing import overload, Literal

# Third-party imports
import numpy as np
import pandas as pd

@overload
def load_data(
    filepath: str,
    usecols: tuple = ...,
    delimiter: str = ...,
    skiprows: int = ...,
    *,
    is_pandas: Literal[False]
) -> np.ndarray: ...
@overload
def load_data(
    filepath: str,
    usecols: tuple = ...,
    delimiter: str = ...,
    skiprows: int = ...,
    *,
    is_pandas: Literal[True]
) -> pd.DataFrame: ...

def load_data(
        filepath: str,
        usecols: tuple = (0, 0),
        delimiter: str = ',',
        skiprows: int = 0,
        is_pandas: bool = False
        ):
    '''
    Load specific columns from a delimited text file into a NumPy array or a Pandas dataframe.

    Parameters:
        `filepath` (str): 
            Path to the file to be loaded.
        `usecols` (tuple of int, optional):
            Tuple (start, end) representing the column range to load (start inclusive, end exclusive).
        `delimiter` (str, optional): 
            Delimiter used in the file. Default is ','.
        `skiprows` (int, optional): 
            Number of initial rows to skip (e.g., header lines). Must be non-negative. Default is 0.
        `is_pandas` (bool, optional): 
            If True, returns a Pandas DataFrame. If False, returns a NumPy array. Default is False.

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
        data = load_data(filepath='data.csv', usecols=(1, 3), skiprows=1)
    '''
    if filepath is None:
        raise ValueError('filepath must be provided')
    if not isinstance(filepath, str):
        raise ValueError('filepath must be a string')
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
    file_path = os.path.join(filepath)
    if is_pandas:
        if usecols == (0, 0):
            data = pd.read_csv(file_path, sep=delimiter, skiprows=skiprows)
        else:
            data = pd.read_csv(file_path, sep=delimiter, skiprows=skiprows, usecols=np.arange(usecols[0], usecols[1]))
    else:
        if usecols == (0, 0):
            data = np.loadtxt(file_path, delimiter=delimiter, skiprows=skiprows)
        else:
            data = np.loadtxt(file_path, delimiter=delimiter, skiprows=skiprows, usecols=np.arange(usecols[0], usecols[1]))
    print('\n=> Data successfully loaded from:\n', file_path)
    print('\n=> data[0:3]:\n', data[0:3])
    print('\n=> Information about the data:')
    print('Type: ', type(data))
    print('Ndim =', data.ndim)
    print('Shape =', data.shape)
    print('Size =', data.size)

    return data